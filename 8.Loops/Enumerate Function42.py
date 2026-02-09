# Enumerate Function
marks=[12,56,32,45,98,12,45,1,4]
index = 0
#index 3 come print -> Ayush ossam
for i in marks:
    print(i)
    if (index == 4):
        print("Ayush, awesome!")
    index+=1
print("code will be complete")

# OR Both code are same...


#Enumerate Function.
# ye loops me index enter kare ga chaye yo string,tuple,list 
for index, mark in enumerate(marks):#enumerate(marks,start=1)--> indexing 0 ki jagh 1 se start hoga.
    print(mark)
    if(index==4):
        print("Ayush , awesome!")

  










