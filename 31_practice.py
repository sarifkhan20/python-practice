words=["donkey","she","her"]
with open("30_file.txt","r") as f:
    c=f.read()

for i in words:
    c=c.replace(i,"#"*len(i))
with open("31_file.txt","w") as f:
    f.write(c)