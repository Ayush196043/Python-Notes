# FILTER FUNCTION
""" use to filter any things Syntex:- filter(predicate, iterable)"""

l =[1,2,3,4,5,6,7]

def filter_function(a):
    return a > 4
new_l =list( filter(filter_function , l))
print(new_l)






















