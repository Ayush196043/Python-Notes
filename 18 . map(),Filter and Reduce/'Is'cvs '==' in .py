# {  'is' vs '==' in python }

#1. both are compare operater

""" 'is' operater use kar ke variable ki property pata kar sakte hai."""

# "is" operater compare karta ka exact location of a menory.

# "==" operater compare the values of memory.

# Example 1:-
print("Example 1:-")
a = 4
b = '4'
print(a is b)# exact location of object in memory

print(a == b) # value
 # "is" me ham ek hi object ok refer karte hai
 # "==" me do object ko compare karte hai.


# Example 2:-
print("Example 2:-")
A = [1, 2, 43]
B = [1, 2, 43]

print(A is B)
print(A == B)

# NOTE :- In csae of Immutable Data type

# Example 3:-
print("Example 3:-")
c = (1,2,3)
d = (1,2,3)
print(c is d)
print(c == d)