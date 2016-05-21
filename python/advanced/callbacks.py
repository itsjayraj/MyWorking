from __future__ import print_function


#regular function with no callback
def fibonacci():
    values = []
    while(True):
        if len(values) < 2:
            values.append(1)
            print(values)

        else:
            values = [values[-1], values[-1] + values[-2]]
            print(values)

        if values[-1] % 17 == 0:
            return values[-1]

        if values[-1] > 10000:
            return

if __name__ == '__main__':
    res = fibonacci()
    if (res != None):
        print(res)