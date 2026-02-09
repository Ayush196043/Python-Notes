# Match case statement.

#Syntax

X = int(input("Enter the number: "))

# matvch the x 
match X:
    
    case 0:
        print("X is zero.")
    case 4:
        print("X is 4.")
    #This statement work as a else.
    case _ :    
        print(X)

         
#In c++ , c and jave use in match case statement break keyword to run the match programe but in python no need to it.

#.Conditional statement use with MATCH case statement.

""" 
    Syntax:-
            match x:
                case _ if...... # Then write the condition.
 """

#Example:-

Y = int(input("Enter the your number: "))

match Y:
# write cases.
    case _ if Y != 90:
        print("Y is not 90.")
    case _ if Y != 85:
        print("Y is not 85.")
    case _ :
        print(Y)













































































    