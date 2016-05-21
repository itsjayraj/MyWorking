class Connection(object):
    counter=0
    max=10
    def __init__(self):
        Connection.checkMaxConnection()
        Connection.counter += 1
        print("connection created {}".format(Connection.counter))

    @staticmethod
    def checkMaxConnection():
        if Connection.max == Connection.counter:
            raise Exception("MAX connection reached {}".format(Connection.counter))
        return True

if __name__ == '__main__':
    for i in range(9):
        Connection()

