# a=1
# b=2
# c=3
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(c>b and c>a):
#         return c
#     else:
#         return b
# print(greatest(a,b,c))


# n=int(input("enter temprature in celsius:"))
# def converter(n):
#     return n+32
# print(converter(n))


# n=int(input("enter number:"))
# sum=0
# def addition(n,sum):
#     if(n==1):
#         return sum+1
#     sum=sum+n
#     return addition(n-1,sum)
# print(addition(n,sum))


# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l

# l=["harry","sarif","an","rohan","subhan"]
# print(rem(l,"an"))


# def rem(l,word):
#     n=[]
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n

# l=["harry","sarif","an","rohan","subhan"]
# print(rem(l,"an"))


def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
multiply(3)