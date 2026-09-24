with open("35_file1.txt") as f:
    content1=f.read()

with open("35_file2.txt") as f:
    content2=f.read()

if(content1==content2):
    print("files are identical")
else:
    print("files are not identical")