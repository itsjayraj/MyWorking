#Always use List pop() and append() because its always O(1)
#other options like pop(index) and insert(index) are expensicve with O(n)


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def revstring(mystr):
    # your code here
    mystack = Stack()
    for ch in mystr:
        mystack.push(ch)
    revstr =''

    while not mystack.isEmpty():
        revstr = revstr + mystack.pop()

    return revstr

if __name__ == '__main__':
    if(revstring('apple') == 'elppa'):
        print('Pass')
    if(revstring('x') == 'x'):
        print('Pass')
    if(revstring('1234567890') == '0987654321'):
        print('Pass')
