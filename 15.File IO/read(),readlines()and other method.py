# read(),readlines()
"""
So many line in file for read each and every line use readline() method

"""
f = open("myfile.txt",'r')

while True:
    line = f.readline()
    print(line)
    if not line:
        print(line, type(line))
        break
    
# Writeline() Method inpython
f = open("Marks2.txt",'w')

lines =['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()















