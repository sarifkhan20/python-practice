word="donkey"
with open("30_file.txt") as f:
    c=f.read()
newC=c.replace(word,"######")
with open("30_file.txt","w") as f:
    f.write(newC)