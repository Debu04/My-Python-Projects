'''
This code will be print the first 50
Fibonacci numbers using While loop

This will print the Fibonacci numbers which is below 50

We know that the First Fibonacci numbers is 0 and 1

So we take a = 0 and b = 1

Then we swapping the values to print the first fibonacci numbers till 50
'''

# Assigning the values
a = 0
b = 1
# Condition the loop will be run to 50
while b <= 50:
    print(b)
    # Swapping the values that is (a) will be (b) and (b) will be (a+b)
    a,b = b,a+b