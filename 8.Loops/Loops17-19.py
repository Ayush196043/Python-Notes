# LOOPS --> some time excute the certen program at a time.
# for loop and while loop.

#FOR loop.
# sequnce list, string tuple,set, dictnori.
list =[ "red","blue","green"]
for i in list:
    print(i)
    for a in i: # nesting is also possible in loop.
        print(a)

# print the number 1 to 50.
for i in range(1,51):
    print(i)

# range(start,end,step)

# While loop.

i=0
while(i < 11):
    print(i)
    i+=1
    

# while loop 
#print 1 to 100.
number=1
while(number<101):
    print(number)
    number+=1

# Amulate DO WHILE LOOPS.
# fist loop is run then after loop depend upon the condition.
i=0
while(True):
    print(i)
    i+=1
    if(i>10):
        break
# BREAK and CONTINUS.
# BREAK-->statement use for out from loop.
# CONTINUS--->statement use for out from iteration.{iteration ko skip kar dego}

for loop in range(20):
    
    if(loop==15):
        print("skip the iteration")
        continue
    print(loop)
        

# else loop with while loop.
num=0
while( num<10):
    print(num)
    num = num +1
else:
    print("Oo ho !")

# pass -> one of the statement in loop and function
