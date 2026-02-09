# Finally keyword.

#  finally hamesha run kare ga is ka important use formation fo function me ho ga jab function ko break 
#karne ke baad koi aor work karna rahe ga tab use karege us work ko finally ke ander.

#syntax:-
#try:
    #statement which could generate
    #exception
#except:
    #solution of generat exception.
#finally:
    #block of code which is going to
    #execute in any situation.


#example:-
def func1():
    try:
        list=[1,2,34,52,67]
        i=int(input("Enter the index: "))
        print(list[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:# ye hamesha run kere ga erroe ho ya na ho.
        print("I am always executed")
        # finally means it is alwaya excuteded.
x=func1()
print(x)

"""
Finelly keyword run that time when both " try" and "except" is not run then finelly keyword is run each and every time.

"""
