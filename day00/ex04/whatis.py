import sys

sys.tracebacklimit = 0

if len(sys.argv) < 2:
    raise SystemExit
if len(sys.argv) > 2:
    raise AssertionError("more than one argument is provided")

try:
    n = int(sys.argv[1])
    print("I'm Even.") if n % 2 == 0 else print("I'm Odd.")
except ValueError:
    raise AssertionError("argument is not an integer") from None
