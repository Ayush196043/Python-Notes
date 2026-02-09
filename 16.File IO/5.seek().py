# SEEK Function "seek()" and TELL Function

with open("5.seek().txt",'r') as f:
    line_1 = f.read()
    print(line_1)
    line_2 =f.seek(6)
    r = f.read(10)
    # line_3 = f.tell()
    # print(line_3)
    print(r)
    a = f.tell()
    print(a)
# Note :-seek(a)- ka use "a" word tak line ko skep kar dega uske baad koi work kara sakte ho read write or append etc. 

# Note :- tell()- ka use position pata karne ke liye kiya jata hai ki is time kaha pe hai.

# Truncate Function : use to control the size of file "truncate(a)":- "a" number of byte hi store rahega in side the file 

