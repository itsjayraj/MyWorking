import itertools

# simple list iter
mylist = [12, 23, 45, 23, 6, 56]
for val in mylist:
    print(val)
print sum(mylist)
print max(mylist)
print min(mylist)
# print index and val
print list(enumerate(mylist))
for idx, val in enumerate(mylist):
    print('index %d val %d' % (idx, val))

# simple string iter
mystring = 'this is my string'
for char in mystring:
    print(char)

# simple dict iter
mydict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
# iter keys
for key in mydict:
    print(key)
# iter values
for val in mydict.itervalues():
    print val
# iter key and val
for key, val in mydict.iteritems():
    print('key %s  val %s' % (key, val))

# iter files
with open('callbacks.py') as myfile:
    for line in myfile:
        print line

# itertools infinite vals
for val in itertools.count():
    if val > 20:
        break
    print val

# merger iter's using zip
idlist = [100, 200, 300, 400, 500, 600, 700, 900, 1, 2, 3]
namelist = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6']
for id, name in zip(idlist, namelist):
    print 'id %s name %s' % (id, name)
print dict(zip(idlist, namelist))


# abstracting/isolating loop conditions
# doing this with yield will be best
def do_something(val):
    print val


def evens(data):
    for val in data:
        if val % 2 == 0:
            yield val


for val in evens(mylist):
    do_something(val)


# writing custom iter
class ToDoList(object):
    def __init__(self):
        self.tasks = []

    def __iter__(self):
        return (task for task in tasks if not task.done)

    def all(self):
        return iter(self.tasks)

    def alldone(self):
        return (task for task in tasks if task.done)


if __name__ == '__main__':
    pass
