
'''
This code is used to get the Factorial of the given number.

To get a Factorial of a number we need to multiply the given number
with the previous number factorial.

Here we know the factorial of 0 that is 1 so we multiply
the numbers to the given number to get the Factorial of the number.
'''

n = int(input('Enter the number '))
# We all know that factorial of 0 is 1
# So we take f = 1
f = 1
# Using a loop we will get the numbers from 1 to n+1
# (n+1) because n is always excluded so we take that
for i in range(1,n+1):
    # By the loop we fetching the number one by one and multiplying it with the previous answer
    f = f*i
# This will only print the factorial of the given number
print(f)