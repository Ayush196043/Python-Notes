# List comprention.--> List comprention is one of the set builder form.
listA=[i for i in range(0,10)]
print(listA)

#Q. print squre of 1 to 10 for using list comprention.
#Solution:-
listB=[i*i for i in range(1,11)]
print(listB)


# USE CONDITIONAL STATEMENT IN LIST COMPRENTION.
list=[i*i for i in range(10) if i% 2==0]
print(list)
list1=[1,2,34]
if 7 in list:
    print("YES")
else:
    print("NO")

#For asking to teacher/ mantore.

A=[1,2,3,4]
B=[6,7,8,(i for i in A)]
print(B)

#nesting in list by using list compranotion.
list2=[i for i in range(0,6)]
list3=[[i for i in range(0,6)],[j for j in range(6,11)]]
print(list3 )

list4=[1,2,3,list2,4,5,list3,6]
print(list4)
print(len(list4))
