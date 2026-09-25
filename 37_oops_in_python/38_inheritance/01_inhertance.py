class Employee:
    company="IITC"
    def show(self):
        print(f"the name of employee  is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company="ITC.infotech"

a=Employee()
b=Programmer()
print(a.company,b.company)