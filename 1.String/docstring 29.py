# DOCSTRING...
# it is writen before function body.
# when docstring is change then program is may or may not be change.

#Example:-1.
def squre(n):
    """Return the square of a number."""
    return n ** 2
print(squre(5))
print("Doc string of squre function",squre.__doc__)

#Example:-2.
def cube(m):
    ''' take in anumber m, return the cube of m'''
    print(m**3)

print(cube(3))
print(cube.__doc__)

#COMMENT:-

# It is write after body of function.
# when comment is change then function is not change.

#Example:
def add(a,b):
    sum= a+b
    return sum
    ''' return adition output of a+b'''#comment hai ye.
print(2,4)   
print(add.__doc__)#--output:- None.



#PEP-8

# in 2001 is writen by Guido Van Rossum, Barrw Warsow and Niek eaghlan.
# focuse of PEP-8 readable, moriable and consistance.

# The ZEN of python 
import this  # output a pome.

#output:The Zen of Python, by Tim Peters

""" Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""


