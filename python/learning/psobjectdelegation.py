"""
Delegation
"""

class nginx(object):
    def __init__(self, state):
        self.state = state

    def __getattr__(self, item):
        return self.state



class server(object):
    def __init__(self):
        self.serve = nginx('ON')

    def __getattr__(self, item):
        return getattr(self.serve, item)

    def __setattr__(self, key, value):
        setattr(self.serve, key, value)


if __name__ == '__main__':
    s=server()
    print(s.state)

    s.state = 'OFF'
    print(s.state)
