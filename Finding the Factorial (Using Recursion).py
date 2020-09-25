
'''

This code is used to get the Factorial of the given number using Recursion.

Recursion means calling the function it self.

'''



def fact(n):
    # We know the factorial of 0 is 1
    # And it is the limit of the recursion
    if n == 0:
        return 1
    # We calling the factorial of the previous number (fact(n-1))
    return n * fact(n-1)


n = 5
result = fact(n)
print(result)