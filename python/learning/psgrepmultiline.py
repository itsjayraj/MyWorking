import re
import sys
import fileinput


search=r'^root.*^games'
filename=r'D:\PythonTraining\day1\passwd.txt'

# search = sys.argv[1]
# filename = sys.argv[2]

with open(filename) as fp:
    m = re.search(search, fp.read(), re.IGNORECASE|re.MULTILINE|re.DOTALL)
    if m:
        print(m.group())
        print(m.span())