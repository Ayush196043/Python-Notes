# #FUNCTION IN PYTHON..
# #Two type function in python.
# # Bilt-in function.Exampel:-()
# # user_deffin_function.

# #User_Deffine_Function.
# def calculate_sum(a,b):
#     sum=a+b
#     print(sum)

# a=10
# b=20
# calculate_sum(a,b)#--> function call.
# # make function used by conditional statement.
# # deffine the function grater number between two number.
# def grater(a,b):
#     if (a>b):
#         print(a,",grater then,",b)
#     elif(b>a):
#         print(b,",grater then,",a)
#     else:
#         print(a,",is equal to,",b)

# grater(a,b)

# # Argument in Function.
# #1.Defalt argument.
# #2.Keyword argument.
# #3.Required argument.
# #4.Variable length argument.

# # Defalt argument.
# def calculate_average(a,b):
#     print("Average: ",(a+b)/2)

# c= 40
# d= 20
# calculate_sum(c,d)
# grater(c,d)
# calculate_average(c,d)

# #keyword argument--> order change ho sakta hai.

# #Required argument.
# def calculate_diff(a,b):
#     print("diffrence: ",(a-b))

# e=10
# f=5
# calculate_diff(e,f)

# def name(fname,mname,lname):
#     print("Hello ",fname,mname,lname)

# name("Mr.Rameshwar","prashad","pandey")

# # Variable Length Argument.
# #argument as a tuple.
# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i   
#     print("Average: ",sum/len(numbers))

# average(10,20,30,40,50,60,70,80,90,100)

#  # dictnery.
# def name(**name):
#     print("hello,",name["Fname"],name["Mname"],name["Lname"])

# name(Fname="ayush",Mname="kumar",Lname="pandey")


# # return condition
# def ayush(m,n):
#     avg= m+n
#     return  avg # function yehi return kare ga.
    
# x=ayush(10,20)
# print(x)

def add(a,b):
    sum = a +b# local
    return 10
c =10
d=20
print(add(c,d))

