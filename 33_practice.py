
with open("32_log.txt") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"present in line: {lineno}")
        break
    lineno +=1
else:
    print("absent")