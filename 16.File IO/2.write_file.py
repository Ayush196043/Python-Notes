# Write the code to writeand creat the file...
f = open("2.write.txt",'w')
f.write("Hii every one i am ayush i am going to work..")
f.close()
# Other type to write the same code for append the line
with open("2.write.txt",'a') as f:
    f.write("Ayush")

# Use to read the code
with open("2.write.txt",'r') as b:
    print(b.read())