#!/usr/bin/env python3
"""Every solution notebook must run clean; every practice check cell must FAIL until you write the code."""
import pathlib, sys
import nbformat
from nbclient import NotebookClient

ROOT = pathlib.Path(__file__).resolve().parent.parent
def run(path, allow_errors):
    nb = nbformat.read(path, as_version=4)
    NotebookClient(nb, timeout=120, kernel_name="python3", allow_errors=allow_errors,
                   resources={"metadata": {"path": str(path.parent)}}).execute()
    return nb

bad = 0
for d in sorted(ROOT.glob("day*_*")):
    try: run(d / "solution.ipynb", False); sol = "ok"
    except Exception as e: sol = f"FAIL ({type(e).__name__}: {str(e).splitlines()[-1] if str(e) else ''})"; bad += 1
    nb = run(d / "practice.ipynb", True)
    checks = [c for c in nb.cells if "check" in c.metadata.get("tags", [])]
    green = sum(not any(o.output_type == "error" for o in c.outputs) for c in checks)
    if green: bad += 1
    print(f"{d.name:18} solution {sol:6} | practice checks red {len(checks) - green}/{len(checks)}")
sys.exit(bad)
