import sys
from near import Near

if len(sys.argv) != 2:
    print """Usage:
    python test_server.py [page_name]
    """
    sys.exit(1)

name = sys.argv[1]

pages = { "near" : Near() }

if name in pages:
    print(pages[name].get())
else:
    print("Invalid page")
