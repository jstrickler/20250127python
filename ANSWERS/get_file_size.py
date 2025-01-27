import sys
import os.path

for f in sys.argv[1:]:
    if os.path.isdir(f):
        print(f"{f} is a directory")
        continue
    else:
        print(f,os.path.getsize(f))
