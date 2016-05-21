def Demo():
    print 'Before 1'
    yield 100
    print 'After 1'

    print 'Before 2'
    yield 101
    print 'After 2'


g = Demo()
value = g.next()
print(value)
print('-----------------------------')
value = g.next()
print(value)
print('-----------------------------')
# value = g.next()
# print(value)