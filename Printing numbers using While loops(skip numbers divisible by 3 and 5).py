'''
 Here this code is used to print the number from 1 to 100 useing While loop
 and skip the numbers which are divisible by 3 and 5
'''


# Initializating n = 1 that means it will be start from 1 till the given number.
n = 1
# Using While loop and give condition to it.
while n <= 100:
    # Applying the skiping part that is skip if the number is divisible by 3 and 5
    if n%3 != 0 and n%5 != 0:
        print(n)
    else:
        pass
# Give increment to the the code.
    n = n+1