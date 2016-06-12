import sys
from near import Near

if len(sys.argv) != 2:
    print """Usage:
    python test_server.py [page_name]
    """
    sys.exit(1)

name = sys.argv[1]

if name == "near":
    z = Near()
    print(z.get())
    sys.exit(0)

print("Invalid page")
