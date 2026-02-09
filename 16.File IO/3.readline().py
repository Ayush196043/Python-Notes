# readline() function is used to the read the file line by line..
with open("3.readline().txt",'r') as a:
    while True :
        line=a.read()
        print(line)
        if not line:
            break
