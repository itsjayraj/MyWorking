import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='Name of the file', nargs='+')
parser.add_argument('-n', '-nn', '-nnn', help='adds line number', action='store_true')
parser.add_argument('-o', '--output', help='output file')

args = parser.parse_args()
#print(args.filename)

temp=None

if args.output:
    temp=sys.stdout
    sys.stdout = open(args.output, 'w')

#for line in file