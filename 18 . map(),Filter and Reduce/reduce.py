from functools import reduce
number = [1,2,3,4,5]

def mysum(x,y):
    return x + y

sum = reduce(mysum ,number)

print(sum)