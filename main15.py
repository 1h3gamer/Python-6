class person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class employee(person):
    def __init__(self,name,idnumber,salary,position):
        self.salary = salary
        self.position = position
        person.__init__(self,name,idnumber)
    def display(self):
        super().display()
        print(self.salary)
        print(self.position)

a = employee("phil", 882906, 20000, "Intern")
a.display()