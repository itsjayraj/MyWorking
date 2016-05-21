"""
a sample py pprogram
"""
from os import listdir

author = "jayraj"


def sqrncube(n=0):
    """
    sqrncube(), finds sqr and cube value of n
    :param n:
    :return:
    """
    return  n**2, n**3


def ls(path='.'):
    """

    :param path:
    :return:
    """
    for file_name in listdir(path):
        print file_name


def main():
    print author
    print sqrncube(5)
    ls()

#main()

if __name__ == '__main__':
    print __name__
    main()
