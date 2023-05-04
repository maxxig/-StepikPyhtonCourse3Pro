from re import fullmatch
import sys

for line in sys.stdin:
    m = fullmatch("_\d{1,}[a-zA-Z]{0,}_{0,1}", str(line).strip())
    print('False' if m is None else 'True')