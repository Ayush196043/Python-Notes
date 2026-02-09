#LISTS IN PYTHON "([])"
"""list have multiple data type in the list like--> int,float,string,etc.
exp--> mix_list=[1,1.0,"jenny",True]
In list have Index,Ordered,Mutable."""


#Print list
number =[12,23,34,24,23]
print("list: ",number)


#Indexing
  #SYNTAX
  #print(list[index]) index started from zero. {indexing me index ko variable ke form me bhi store kar sakete hai like--> A=list[index]}
   
print("index: ",number[3])

 
#Slicing of list 
    #SYNTAX
    #list[starting index: end index]
                                    #In slicing end index is not concider..
print("slicing: ",number[0:4])
#list[ : ] means slice list from zero index to length of list.
#JUMP SLICING--->list[starting:end:jump step]
print("jumpinng slicing: ",number[2:5:2])


#METHOD FO LIST 
""" 1. list.sort()
print(list) # arrange in ascending order.
2. list.sort(reverse=True)
print(list) #arrange in deascendiung order.

3. list.reverse()
print(list) # reverse the list.

4. list.append(element)
print(list) # add element in the list.

5. list.insert(index,element)
print(list) # insert element in the list.

6. list.extend([element1,element2........])
print(list) # add multiple element in the list.

7. list.remove(element)
print(list) # remove element from the list.

8. list.pop(index)
print(list) # remove element from the list.

9. list.clear()
print(list) # clear the list.

10. list.copy()
print(list) # copy the list.

11. list.count(element)
print(list) # count the element in the list.

12. list.index(element)
print(list) # find the index of element in the list."""
#List have so many other function we learns these function by work or solve the qustion and search these function in CHATGPT or an other resource.

#Example of the functions of the list..

number =[12,23,34,24,23]
print("count the number: ",number.count(34))

print("find the index: ",number.index(34))

number.sort()
print("short the list: ",number)
number.sort(reverse=True)
print("short the list in reverse: ",number)
number.reverse()
print("reverse the list: ",number)


number.remove(23)
print("remove element in the list: ",number)
number.pop(2)
print("remove element in the list: ",number)
number.clear()
print("clear the list: ",number)



number.append(23)
print("add element in the list: ",number)
number.insert(3,56)
print("insert element in the list: ",number)
number.extend([12,23,34])
print("add multiple element in the list: ",number)
number.copy()
print("copy the list: ",number)











































