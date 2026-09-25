class Employee:
    name="sarif"  #class attribute
    age=20
    language="python"

    def getinfo(self):
        print(f"the language is {self.language}.the name is {self.name}")
    
    def greeting(self):
        print("Hello ji!!")


don=Employee()
# don.name="bawligend"  #instance attribute
don.getinfo() # == Employee.getinfo(don)
don.greeting()