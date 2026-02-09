#RECYRSION.

#recursion is a function in side same function.
# Break the problem into smaller sub-problems.
# Recursion is a programming technique where a function calls itself to solve a problem.

# Example:-
def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

print("factorial",factorial(5))


# write a program to print the faibonacci sequence.

# Logic:-
# F(0) = 0, F(1) = 1
# F(2) = F(1) + F(0)
# F(n) = f(n-1) + F(n-2)
# 1 1 2 3 5 8.....

# CODE:-

def faibonacci(m):
    if ( m<0):
        print("Incorrect")
    elif(m==0):
        return 0
    elif(m==1):
        return 1
    else:
        return faibonacci(m - 1) + faibonacci(m - 2)
    
print("faibonacci",faibonacci(9))

# byusing loops:-
n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
