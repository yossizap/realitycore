import sys
import re

with open(sys.argv[1], "rb") as f:
    content = f.read()
with open(sys.argv[1], "wb") as f:
    content = re.sub(b"python27.dll", b"dice_py.dll\0", content)
    f.write(content)