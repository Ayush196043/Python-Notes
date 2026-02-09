#SET - is a collection of unorddered element.every element is uniqe and immutable.
# set is mutable. Set have different data type.
#set do not have dublecat value.empty set is dinoted by---> set1=set() [set1 is a empty set.]
#indexing not in set.

#METHOD OF SET.
#set.add(element)---> add the element in set.
#set.remove(element)---> remove the element in set.
#set.discard(element)---> remove the element in set.
#set.pop()---> remove the random element.
#set.clear()--->clear the set.

#OPERATION OF SET.
# set.unoin(set2)--> combine the both set.[set|set2] '|'--> union.
# set.update(set2)-->combine the both set.[set|=set2].

# set.intersection(set2)--> take commen from both set.
# set.intersection_update(set2)---> take commen from both set.
#Exemple:- [intersection , intersecton_update]
set1={ "ayush","vivak","maths"}
set2={"maths","physics","chemistry"}
print("take intersection",set1.intersection(set2))
set1.intersection_update(set2)
print("intersecton_update",set1)

#differance , symmetric_differance{(A | B) - (A & B)}.
# set.differance(set1)---> output is a set is not commen in set1.
# set.differance_update(set1)--> output is a set is not commen in set1.
#Exemple:-
set3={1,2,3,4,5}
set4={4,5,6,7}
print("differance: ",set3.difference(set4))
set3.difference_update(set4)
print("differance_update: ",set3)

#set.symmetric(set2)---> {(A | B) - (A & B)}.
#set.symmetric_update(set2)---> {(A | B) - (A & B)}.
#Example:-
set_A={1,2,3,4,5,6}
set_B={4,5,6,7,8,9}
#print("symmetric_difference: ",set_A.symmetric_difference(set_B))
#print("symmetric_update: ",set_A.symmetric_difference _update(set_B))


# Type of set.
# set1.isdisjoint(set2)---> intersection of both set is empety.
#set1.issubset(set2)---> set1 is a subset of set2 if every element of set1 in set2.{<=}
#set1.issuperset(set2) ---> set1 is a superset os set2 if every element of set2 in set1.{>=}
 # del set ---> delete the set.
