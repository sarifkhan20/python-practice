class Grandparent:
    def __init__(self):
        self.name = "Sarif"
        print("Grandparent constructor")


class Parent(Grandparent):
    def __init__(self):
        # super() calls the constructor of the immediate parent class
        # Here, Parent's immediate parent is Grandparent
        super().__init__()

        self.age = 20
        print("Parent constructor")


class Child(Parent):
    def __init__(self):
        # super() calls Parent's constructor
        # Parent's constructor will then call Grandparent's constructor
        super().__init__()

        self.college = "JECRC"
        print("Child constructor")


# Creating an object of Child
c = Child()

print(c.name)
print(c.age)
print(c.college)