# Loops :- When we write the same code more time the we use loops.
""" They are three types:- 1.For loop   2.While loop  3.Do-While loop"""

# For loop :- This loop use that time when we know how many time loop is run....
# While loop :- This loop use that time when we do not know how many time loop is run..


# Example 1.:- Print the first 10 natural numbers using for loop.
n = 11
for i in range(1,n):
    print(i) #Output:- 1,2,3,4,5,6,7,8,9,10..

# Example 2:- Python program to print all the even numbers within the given range.

starting = int(input("Enter your starting number: "))
Ending = int(input("Enter your ending number: "))

for i in range(starting,Ending):
    if (i % 2 == 0):
        print(i)  # you can free to print any range of number find the even number..

# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.

number = int(input("Enter the number: "))
sum=0
for i in  range(1,(number)+1):
    sum+=i
print(sum)

    



























































