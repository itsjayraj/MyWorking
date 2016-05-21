class Demo(object):
    #its a static data member always
    lang = 'python'
    def __init__(self, pm):
        #print("am the constrctor {}".format(self))
        self.package_manager = pm

    #this is instance method not statuc
    def get_pkg_manager(self):
        return self.package_manager

    def __del__(self):
        print("am at destructor {}".format(self))


if __name__ == '__main__':
    d=Demo('pip')
    print(d)
    print(d.get_pkg_manager())
    #this below statement throws error since its instance method
    #print(Demo.get_pkg_manager())