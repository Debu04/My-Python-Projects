'''
This code is used to print the star pattern using the For loop

The star pattern will be in descending order
'''

# Here the range will be start from 4 to 0 (This For will print the numbers of Raw)
# It will be in descending order so we use -1 at the end of it
for i in range(4, 0, -1):
    # This for loop will go till (i) and This will print the numbers of columns
    for j in range(i):
        # This pattern will print according to the loops
        print("#", end=" ")
    # The empty print statement will generate new lines at the end of the every line.
    # That means the results will be start from a new line
    print()

# The result of the code
                # # # #
                # # #
                # #
                #