#Dictnory---("dict")
#:- Dictinory is a well mantain order collection of  keys and values.
dict={'name':'ayush', 'age':20,'DOB':"14/02/2005"}
print(type(dict))
print(dict)
print(dict['name'])# jab key dict me exixt nahi kare gi to ye error dega.
#but
print(dict.get('name'))# jab key dict me nahi rahe ga to ye None print kare ga.

# accesing the keys and values.

#dict.keys()--> it give the all keys those present in dict.
#dict.values()--> it give the all values present in dict.

#Example:-
import time
dict1={"name":"harsha","corce":"Btech","Branch":"AI"}
print(dict1.keys())
print(dict1.values())
for key in dict1.keys(): 
    time.sleep(3)
    print(dict1[key])

                                                                                                   
#Accesing the all key and values at a time.

#dict.items()-->it gives the all key valuse paire.
#Example:-
a={'MS.Dhoni':56,'Virat':100,'KL Rahul':111}
print(a.items())



#method of dicionary.

#dict.update(__)
#example:-
ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.update(ep2)
print(ep1)

#clear()--> clear the all keys and values pair in dictionary.
ep1.clear()
print(ep1)#output-->{}(empty dict)


#dict.pop(key)--> it is remove the key values pair.
A={'name':'ayush','cgpa':8.5,'marks':[87,78,75]}
A.pop('name')
print(A)#output:{'cgpa':8.5,'marks':[87,78,75]}
#but--> print(A.pop('name'))output--> ayush

#dict.popitem()--> it remove the last element from the dicionary.
A.popitem()
print(A)# remove the last element from dict.


# del -->we can also usse the del key word remove the del key word.
#del dict--> dilete the dictionary.but when you pass the key then discard these key.
