# p1="make money"
# p2="dream big"
# p3="sleep good"
# p4="work hard"

# message=input("enter you comment:")

# if((p1 in message) or(p2 in message) or (p3 in message) or (p4 in message)):
#     print("this comment is spam")

# else:
#     print("it is not")




# l=["sarif","harshit","divya","himanshi"]
# name=input("enter name")

# if(name in l):
#     print("you name is in list")

# else:
#     print("your name is not in list")




marks=int(input("enter input"))
if(marks<=100 and marks>80):
    grade="A"

elif(marks<80 and marks>=70):
    grade="B"

elif(marks<70 and marks>=50):
    grade="C"

elif(marks<50 and marks>=40):
    grade="D"

else:
    grade="FAIL"

print(grade)