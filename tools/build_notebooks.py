#!/usr/bin/env python3
"""Generate dayN/practice.ipynb and dayN/solution.ipynb from the dayN/s*.py + kata.py snippets.

The .py files are the source of truth. Per snippet, top-level statements are split into
  solution code  (what you write)  and  check code (asserts that use what you wrote).
Practice = empty attempt cells + live check cells. Solution = same layout, attempts filled in.
"""
import ast, copy, pathlib, re
from nbformat import write
from nbformat.v4 import new_code_cell as code, new_markdown_cell as md, new_notebook

ROOT = pathlib.Path(__file__).resolve().parent.parent
POOL_NOTE = ("Notebook note: process-pool workers must live in an importable module (spawned children "
             "can't see functions defined in cells), so the worker is written with `%%writefile`.")
OVERRIDES = {  # snippets that need notebook-specific code: [(solution, check), ...]
    "day3_cli/s7_concurrency.py": [
        ("%%writefile _pool_worker.py\ndef sq(n): return n * n", ""),
        ("import importlib; importlib.invalidate_caches()\nfrom concurrent.futures import ProcessPoolExecutor\n"
         "from _pool_worker import sq\n\nwith ProcessPoolExecutor(2) as ex:\n    r = list(ex.map(sq, range(5)))",
         "assert r == [0, 1, 4, 9, 16]")],
    "day6_pipeline/s7_concurrency.py": [
        ("%%writefile _pool_worker.py\ndef cpu(n): return sum(i * i for i in range(n))", ""),
        ("import importlib; importlib.invalidate_caches()\nfrom concurrent.futures import ProcessPoolExecutor\n"
         "from _pool_worker import cpu\n\nwith ProcessPoolExecutor(2) as ex:\n    r = list(ex.map(cpu, [1000] * 4, chunksize=2))",
         "assert r == [cpu(1000)] * 4")],
}


def has_assert(n): return any(isinstance(x, ast.Assert) for x in ast.walk(n))
def stores_all(n):
    out = set()
    for x in ast.walk(n):
        if isinstance(x, ast.Name) and isinstance(x.ctx, (ast.Store, ast.Del)): out.add(x.id)
        elif isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): out.add(x.name)
        elif isinstance(x, ast.ExceptHandler) and x.name: out.add(x.name)
        elif isinstance(x, ast.arg): out.add(x.arg)
    return out
def stores_top(n):
    """Names bound at module scope by this statement (don't descend into function/class/lambda/comprehension)."""
    out = set()
    def walk(x):
        if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): out.add(x.name); return
        if isinstance(x, (ast.Lambda, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)): return
        if isinstance(x, ast.Name) and isinstance(x.ctx, (ast.Store, ast.Del)): out.add(x.id)
        if isinstance(x, ast.ExceptHandler) and x.name: out.add(x.name)
        for c in ast.iter_child_nodes(x): walk(c)
    walk(n)
    return out
def free_loads(n):
    loads = {x.id for x in ast.walk(n) if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Load)}
    return loads - stores_all(n)
def import_names(n):
    return {(a.asname or a.name.split(".")[0]) for a in n.names}
def is_run(n):
    return (isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and ast.unparse(n.value.func) == "asyncio.run")


class AwaitRun(ast.NodeTransformer):  # notebooks already run an event loop: asyncio.run(x) -> await x
    def visit_Call(self, n):
        self.generic_visit(n)
        return ast.Await(n.args[0]) if ast.unparse(n.func) == "asyncio.run" else n


def parse_snippet(path):
    src = path.read_text()
    lines, tree = src.splitlines(), ast.parse(src)
    body, doc = tree.body, ast.get_docstring(tree)
    prev = body[0].end_lineno if isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) else 0
    stmts = body[1:] if prev else body
    chunks = []
    for n in stmts:
        text = "\n".join(lines[prev:n.end_lineno]).strip("\n")
        if "asyncio.run" in text:
            text = ast.unparse(ast.fix_missing_locations(AwaitRun().visit(copy.deepcopy(n))))
        chunks.append((n, text))
        prev = n.end_lineno
    notes = [l.lstrip("# ").rstrip() for l in lines[prev:] if l.strip()]
    return doc, chunks, notes


def segments_for(chunks):
    """Group statements into units, classify as solution (S) or check (C), return [(S_src, C_src)]."""
    units = []  # [nodes, text, kind]
    for n, text in chunks:
        if (units and is_run(n) and isinstance(units[-1][0][0], ast.AsyncFunctionDef)
                and ast.unparse(n.value.args[0].func) == units[-1][0][0].name):
            units[-1][0].append(n); units[-1][1] += "\n" + text; continue
        units.append([[n], text, None])
    imports = {}
    for nodes, text, _ in units:
        if isinstance(nodes[0], (ast.Import, ast.ImportFrom)):
            for name in import_names(nodes[0]): imports[name] = text
    cands = [u for u in units if any(has_assert(n) for n in u[0]) and not isinstance(u[0][0], (ast.ClassDef,))
             and (not isinstance(u[0][0], (ast.FunctionDef, ast.AsyncFunctionDef)) or len(u[0]) > 1)]
    sol_defined = set()
    for u in units:
        if u not in cands and not isinstance(u[0][0], (ast.Import, ast.ImportFrom)):
            for n in u[0]: sol_defined |= stores_top(n)
    targets, needed = [], set()
    for u in units:
        if u in cands:
            free = set().union(*(free_loads(n) for n in u[0])) - set().union(*(stores_all(n) for n in u[0][:1]))
            u[2] = "C" if free & sol_defined else "S"
            if u[2] == "C": needed |= free & sol_defined
            if u[2] == "S" and isinstance(u[0][0], ast.Assert):
                targets += masked(u[0][0])
        else:
            u[2] = "S"
    segs = []
    for nodes, text, kind in units:
        if kind == "S":
            if not segs or segs[-1][1]: segs.append([[], []])
            segs[-1][0].append(text)
        else:
            if not segs: segs.append([[], []])
            segs[-1][1].append((nodes, text))
    out = []
    for s, c in segs:
        pre, seen = [], set()
        for nodes, _ in c:
            for n in nodes:
                for name in sorted(free_loads(n)):
                    if name in imports and imports[name] not in seen: seen.add(imports[name]); pre.append(imports[name])
        ctext = "\n".join(pre + ([""] if pre else []) + [t for _, t in c]) if c else ""
        out.append(("\n".join(s), ctext))
    return out, targets, sorted(needed)


def masked(a):
    t = a.test
    parts = t.values if isinstance(t, ast.BoolOp) and isinstance(t.op, ast.And) else [t]
    return [f"assert ⟨your expression⟩ == {ast.unparse(p.comparators[0])}" for p in parts
            if isinstance(p, ast.Compare) and len(p.ops) == 1 and isinstance(p.ops[0], ast.Eq)]


def build_day(day_dir):
    files = sorted(day_dir.glob("s*.py")) + [day_dir / "kata.py"]
    title = next(l for l in (day_dir / "README.md").read_text().splitlines() if l.startswith("# "))
    nbs = {k: [md(f"{title} ({k})\n\n" + ("Rebuild each snippet from a blank page; **check** cells go green when you're right. "
                                          "Stuck? Peek at `solution.ipynb`, then redo it from memory." if k == "practice" else
                                          "Reference solutions. Every cell is runnable; `practice.ipynb` is the blank-page twin."))]
           for k in ("practice", "solution")}
    for f in files:
        key = f"{day_dir.name}/{f.name}"
        doc, chunks, notes = parse_snippet(f)
        if key in OVERRIDES: segs, targets, needed, notes = OVERRIDES[key], [], [], [POOL_NOTE] + notes
        else: segs, targets, needed = segments_for(chunks)
        head = f"## `{f.name}`: {doc.split(': ', 1)[0].split(' ', 2)[-1]} — {doc.split(': ', 1)[-1]}"
        names = ("\n\nThe checks expect your code to define: " + ", ".join(f"`{n}`" for n in needed)) if needed else ""
        extra = names + (("\n\nMake these true (write your own expression):\n\n" + "\n".join(f"- `{t}`" for t in targets)) if targets else "")
        tail = "\n".join(f"- {n}" if n.startswith(("VARIATION", "KATA")) else n for n in notes)
        for kind, nb in nbs.items():
            nb.append(md(head + (extra if kind == "practice" else "")))
            for i, (sol, chk) in enumerate(segs):
                if sol:
                    c = code(sol if kind == "solution" else f"# your code ({f.stem}, part {i + 1})" if len(segs) > 1 else f"# your code ({f.stem})")
                    c.metadata["tags"] = ["attempt"]; nb.append(c)
                if chk:
                    c = code(chk); c.metadata["tags"] = ["check"]; nb.append(c)
            if tail: nb.append(md("**Then, vary it:**\n\n" + tail))
    for kind, cells in nbs.items():
        nb = new_notebook(cells=cells, metadata={"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}})
        write(nb, day_dir / f"{kind}.ipynb")


if __name__ == "__main__":
    for d in sorted(ROOT.glob("day*_*")): build_day(d)
    print("notebooks built")
