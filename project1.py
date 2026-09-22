import random
computer=random.choice([-1,0,1])
youstr=input("enter your choice")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"s",-1:"w",0:"g"}
you=youdict[youstr]
print(f"you choose {reversedict[you]}")
print(f"computer choose {reversedict[computer]}")
if(computer==you):
    print("its a draw")
else:
    # if(computer==-1 and you==1):
    #     print("you win!")
    # elif(computer==-1 and you==0):
    #     print("you lose!")
    # elif(computer==1 and you==-1):
    #     print("you lose!")
    # elif(computer==1 and you==0):
    #     print("you win!")
    # elif(computer==0 and you==1):
    #     print("you lose!")
    # elif(computer==0 and you==-1):
    #     print("you win!")
    if((computer-you)==2 or (computer-you)==-1):
        print("you lose")
    else:
        print("you win")
        