# Raising Custom Error in Python.
# In Python , we can raise custom errors by using the raise keword.


#Example:-
# a=int(input("Enter any value between 5 to 9: "))

# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")
# print(a)


#Definining Custom Exceptions.
# class CustomErroe(Exception):
#     #code
#     pass

#Enter the number between 5 to 9 then coce will be run
#and user input is quit then progrem is also run other
#wise program is not run.

#CODE:-

b=(input("enter the number between 5 and 9: "))
if(b=="quit"):
    print(b)
elif(int(b)<5 or int(b)>9):
    raise ValueError("enter the number between 5 and 9")
