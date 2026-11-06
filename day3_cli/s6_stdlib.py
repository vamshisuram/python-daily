"""D3 P6 Stdlib: re named groups, shlex, subprocess, textwrap."""
import re, shlex, subprocess, sys, textwrap

m = re.match(r"(?P<lvl>ERROR|INFO): (?P<msg>.*)", "ERROR: disk full")
assert m["lvl"] == "ERROR" and m["msg"] == "disk full"
assert re.sub(r"\d+", "#", "a1b22") == "a#b#"
assert shlex.split('a "b c" d') == ["a", "b c", "d"]
r = subprocess.run([sys.executable, "-c", "print('hi')"], capture_output=True, text=True, check=True)
assert r.stdout.strip() == "hi"
assert textwrap.dedent("  a\n  b") == "a\nb"
# VARIATION: compile the regex with re.VERBOSE and comments
# VARIATION: make subprocess fail; catch CalledProcessError and read .returncode
