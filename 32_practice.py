with open("32_log.txt") as f:
    content=f.read()
if("python" in content):
    print("present")
else:
    print("absent")