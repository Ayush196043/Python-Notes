#Tuple.

# Tuple is denoted by '()'.
tuple = (1,2,3,4)
print(type(tuple))
tuple1=(1,1,2,3,4)
print(tuple1)#repesentation is alowed.
tuple2=(1,"jenny",2,"Python",2.5,)
print(tuple2)# use more then one datatype in one tuple.

#INDEXING IN TUPLE in python is same as indexing in list.
#slicing is also same.

#Nesting in tuple is possible.
tuple3=(1,2,(3,4,5),6,7)
print("nested in tuple: ",tuple3[2][1])

# single element in tuple.
tuple4=(10,)#tuple4=(10)--->print(type(tuple4))-->output:- <class 'tuple'>
print(tuple4)

a = tuple4*5
print(a)# multiple time print.

# Method of tuple..
""" min() and max()--> only used for integer.
tuple.count(element)--> number of time element occer in tuple.
tuple.index(element)--> find the element occer first."""

