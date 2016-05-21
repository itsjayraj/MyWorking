import re
import sys
import fileinput

search = sys.argv[1]

filename = sys.argv[2]

for line in open(filename, 'r'):
    if re.search(search, line):
        print line,
        if line == None:
            print 'no matches found'


# for line in fileinput.input():
#     if re.search(search, line):
#         print "{:>6} {}".format(fileinput.lineno(), line)