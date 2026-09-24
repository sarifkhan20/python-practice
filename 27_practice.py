f=open("27_poem.txt")
c=f.read()
if("twinkle" in c):
    print("the word is present")
else:
    print("it is not present")
f.close()