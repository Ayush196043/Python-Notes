# f = open('myfile2.txt', 'w')
# print(f)# Output: - name = myfile.txt , mode=read
# open() is function that can give the commend to open the file.
# File have sone mode Like('r'->for reading, 'w'-> for writing and 'a' for appending)

# For read the file content

# text = f.read()
# print(text) # Output:- Hey herry aweson man
# f.close()

#"""

#They are various method to open the files.
"""
 1. read(r):- This method opens the file for reading only and give error when they do not exixt. This mode is defalt mode.

 2. write(w):- This mode open the file writing only and creats a new file does not exist
  
3. Append(a) :- This mode open the file for appending only and creates a new file if the file donot exist. """

"""
4. """
# This few line code show that write the file
T = open("myfile2.txt",'w') 

book = T.write("Hii Every one file 'myfile2.txt' is a liberay file they have contane so many books")
print(book)
T.close()

# This few code for read the file.
f = open("myfile.txt", 'r') # ---> Read mode in work as by defalt..
text = f.read()
print(text)
f.close

# This few line code for append the some line in the file.
# we use appand mode that time when we have write the some taxt without delete the text then use appind mode.

P = open("myfile2.txt", 'a')
black =P.write("Hii everyone the line is appended in the file 'myfile2.txt'.")
P.close()

# This few line code for create(x):- This mode creat the file when file alrady present then through error.

# Text (t):- "rt"->thhis means file read as text file.
# Binary(b):-"rb"->this means file read as binery.


# With statement.--> use automaticaly closed the file.
with open('myfile.txt', 'a')as f:
    f.write("Hello World")




































































































