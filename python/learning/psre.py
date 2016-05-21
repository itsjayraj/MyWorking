import re

s = 'the python and the python and pearl scripting'

m = re.match('python', s)
if m:
    print('match found')
else:
    print('match not found')


m1 = re.search('python', s)
if m1:
    print('match found')
else:
    print('match not found')


m2 = re.search('p.*N', s, re.IGNORECASE)
if m2:
    print('match found')
    print(m2.group())
    print(m2.span())
else:
    print('match not found')


m3 = re.search('p.*?N', s, re.IGNORECASE)
if m3:
    print('match found')
    print(m3.group())
    print(m3.span())
else:
    print('match not found')

for m4 in re.finditer('python', s):
    print(m4.group())
    print(m4.span())