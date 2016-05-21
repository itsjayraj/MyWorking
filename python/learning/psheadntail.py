import io
import os


def headntail(filename, **kwargs):
    valid_keys = ['count', 'order']

    for param in kwargs:
        if param not in valid_keys:
            raise TypeError("Error message")

    order = kwargs.get('order', 'head')
    count = kwargs.get('count', 10)

    if order == 'head':
        content = open(filename).readlines()[:count]
    elif order == 'tail':
        content = open(filename).readlines()[-count:]

    return ''.join(content)


if __name__ == '__main__':
    print headntail("D:\PythonTraining\day1\passwd.txt", count=2, order='head')