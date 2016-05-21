class Person(object):
    def __init__(self, name, gender):
        self.__name = name
        self.gender = gender

    def get_info(self):
        print("name: {}".format(self.__name))
        print("gender: {}".format(self.gender))



if __name__ == "__main__":
    p=Employee(name="MyName", gender="male")
    p.get_info()
    print p.gender
    print p.__name
