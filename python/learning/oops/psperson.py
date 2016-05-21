class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_info(self):
        print("name: {}".format(self.name))
        print("gender: {}".format(self.gender))


class Employee(Person):
    def __init__(self, eid, name, gender, dept, desig):
        self.eid = eid
        self.dept = dept
        self.desig = desig
        #in reference to the current obj call the base class of employee
        super(Employee, self).__init__(name, gender)

    def get_info(self):
        print("eid: {}".format(self.eid))
        super(Employee, self).get_info()
        print("department: {}".format(self.dept))
        print("designation: {}".format(self.desig))
        

if __name__ == "__main__":
    #p=Employee(name="MyName", gender="male")
    p=Employee("12345", "sam", "male", "sales", "clerk")
    p.get_info()
    print(type(p))