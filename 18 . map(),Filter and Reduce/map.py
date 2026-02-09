# MAP FUNCTION
#Syntex:- map(functon , iterable)

cube = lambda x: x**3

l = [1,2,3,4,5]
# new_l =[]
# for item in l:
#     new_l.append(cube(item))
# print(new_l)
# or
new_l =list( map(cube,l))
print(new_l)





