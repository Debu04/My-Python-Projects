'''
This code is used to print the perfect square numbers
 using for and While loop from 1 to 500

This code also helpful to compare both the For and While loop
that how the same thing written on both loops.

This will print the results only
'''


                                                # For loop
print("For loop results")
# Starting the For loop from 1 to 500
for i in range(1,500):
    # Condition if the current number(i) square is less than 500
    # Here i**2 means that current number power is 2
    if i**2<=500:
        # Print the square number
        print(i**2)



                                                # While loop
print("While loop results")

# It means the loop will be start from 1
j = 1
# Providing condition if the number(j) square is less than equal to 500
while j**2 <= 500:
    # Print the square of the number
    print(j**2)
    # Providing the increment for the While loop
    # So the loop will be check the numbers one by one till the given numbers
    j = j + 1