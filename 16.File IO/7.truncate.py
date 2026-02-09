with open("7.truncate.txt",'w') as f:
    f.write("hello world!")
    f.truncate(5)
with open("7.truncate.txt",'r') as f:
    print(f.read())