
'''
Using while loop printing the # pattern that contains
4 raws and 5 colomuns
'''


# Initialzing the i= 1
i =1
# It will starts from i to 4 (This will print the number of raws)
while i <=4:
    # Initialzing the j= 1
    j = 1
    # It will starts from j to 5 (This will print the numbers of colomuns)
    while j<=5:
        # Assigning the printing sign (#) and (end = " ") will add some extra space between the signs
        print("#",end=" ")
        # Give increment to the j loop
        j = j + 1
    # Give increment to the i loop
    i = i +1
    # The empty print statement will generate new lines at the end of the every line.
    # That means the results will be start from a new line
    print()