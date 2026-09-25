from random import randint
class Train:
    def __init__(self,trainno):
        self.trainno=trainno

    def book(self,fro,to):
        print(f"you train {self.trainno} is booked from {fro} to {to}")

    def getstatus(self):
        print(f"you train {self.trainno} is running successfully")

    def getfare(self,fro,to):
        print(f"you train {self.trainno} is booked from {fro} to {to} with the fare {randint(100,1000)}")

t=Train(12399)
t.book("rampur","delhi")
t.getstatus()
t.getfare("rampur","delhi")
