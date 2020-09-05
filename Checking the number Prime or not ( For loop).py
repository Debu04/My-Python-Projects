
'''
This code is used to check whether the number is a prim number or not

First it will take the input from the user and
using for loop it will check  the number that it is divisible by any number or not

The For loop will start from 2 to the given number
'''



n = int(input("Enter the number that you want to check prime or not "))
for i in range(2,n):
    if n%i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")