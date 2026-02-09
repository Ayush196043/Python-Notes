# SET FUNCTION..
"""set.add(element)---> add the element.
set.remove(element)---> remove the element first occerance.
set.clear( )---> empty the set.
set.pop( )--> removr the any random element.
set.union(set2)---> write the element in a single set.
set.intersection(set2)---> commen element write a one set."""
set={1,2,3,4,5}
print(set)

# creat a empty set 
# set= set()---> only this is work.print(type(set))--> <class 'set'>
# set ={}---> print(type(set))--> output(<class ' dict'>)
# add the element in set use 
# set.add(element)
#remove the element.
#set.remove(element)
set1={1,2,3,4,5,6}
#set1.remove(7)#--->output give keyError.
#set.discard(element)
#set1.discard(7)#can not give any error
set1.pop()
print(set1)

# set operstion.
# set.union(set2)---> all element in one set combine.union-->'|'
#set.intersection(set2)--> commen element in a set.intersection-->
#symmetric difference[(set1 | set2) - (set1 intersection set2)]
set2={'Ram','Shyam','jenny'}
set3={'jenny','jiya','Aakash'}
a=set2.union(set3)
print(a)
b=set2.intersection(set3)
print(b)
set2.update(set)# set2|=set(union update)
print(set2)
#intersection--->(&)sign.
print("intersection",set2.intersection(set3,set))
set2.intersection_update(set3)
print(set2)
print(set3)
#union update.
set4={12,13}
set4.update(['ayush', 'pandey'])
print(set4)

# differance and symmetric difference. update also.
#set1.differance(set2)--> it will give the element is set1 but not in set2.
#set1 - set2--> same out put as set1.differance(set2)
set_diff={'ram','vivak'}
set_diff.difference(('om','saurabh'))
print("differance",set_diff)

#st1.differance_update(set2)--> it will be give element in set1 not in set2.

#set.symmetric_diffeerence(set) # '^'
set9={'ram','ashutosh'}
print(set9.symmetric_difference(set_diff))#return all the element either in set1 and set2 but not in commen.
#symmetric_difference not allow on multiple set but ^ use in multiple set.



