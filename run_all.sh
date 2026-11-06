#!/usr/bin/env bash
# Run every snippet; each self-checks with asserts. Usage: ./run_all.sh [day_dir]
fail=0
for f in ${1:-day*}/*.py; do
  if python3 "$f" >/dev/null 2>&1; then echo "ok   $f"; else echo "FAIL $f"; fail=1; fi
done
exit $fail
