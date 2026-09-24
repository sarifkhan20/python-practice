with open("37_old.txt") as f:
    content=f.read()

with open("37_new.txt","w") as f:
    f.write(content)