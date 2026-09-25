class Employee:
    name="sarif"  #class attribute
    age=20
    language="python"
    
    def __init__(self,name,age,language):
        self.name=name
        self.age=age
        self.language=language
        print("i am a constructo i am being runned without calling") #dunder method which is automatically called ,these methods starts with "__"

    def getinfo(self):
        print(f"the language is {self.language}.the name is {self.name}")
    
    def greeting(self):
        print("Hello ji!!")


don=Employee("khan",13000,"c++")
print(don.name,don.language) 