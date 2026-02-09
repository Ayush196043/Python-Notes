# Exception Handling.
""" Exception Handling to use manupulate the erroe who's comming  """

a = input("Enter the number: ")
print(f"Multiplacation table of {a} is: ")

try: # ( in try we write the those code where error may be come.)
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e: #( In use of "except" word to manage the error in code.)
    print("sorry some error occurred")

# Note we can handel spacfic type fo error by use this SYNTAX-(except write type of error)
 # Example:-
a = input("Enter your number: ")
print(f"Print the square and cube of {a} ")

try:
    print(f"{int(a)**2 & int(a)**3}")

except ValueError:
    print("input gives ValueError")


# In Exception Handlnig after "rty,except" key word we use "finally" Kyeword.
""" 
In finaly keyword use that time run the code when the in above the programe give the ERROR then we use the finally Keyword to execute the remain code without any restiction.

"""























