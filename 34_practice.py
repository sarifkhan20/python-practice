with open("34_this.txt") as f:
    content=f.read()

with open("34_copied.txt","w") as f:
    f.write(content)