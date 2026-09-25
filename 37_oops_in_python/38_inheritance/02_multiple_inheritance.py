class Employee:
    company="IITC"
    name="default"
    salary=10000
    def show(self):
        print(f"the name of employee  is {self.name} and the salary is {self.salary}")

class Coder:
    language="python"
    def printlanguages(self):
        print(f"out of all langauage,yours is {self.language}")

class Programmer(Employee,Coder):
    company="ITC.infotech"
    def showlanguages(self):
        print(f"the name is {self.name} and he is good with {self.language} language")

a=Employee()
b=Programmer()
b.show()
b.printlanguages()
b.showlanguages()
print(b.company)