# Local Variable:- Those variable in function is called local variable
# Globle Variable:- Those variable not in function but use in functon as well as in out 
# of the function is called in globel variable.

# x = 4
# print(x)

# def hello():
#     global x
#     x = 10
#     print(x)

# hello()
# print(x)

y = 20
print(y)


def book():
    global y
    y = 25
    print(y)

book()
print(y)#-----> y = 25 is a global 

























































