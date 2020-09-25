'''

This code is used to take the inputs 5 names from the user and
print the names if that have more than 5 letters.

'''




# Creating a search name function.
def search(list):
    length = 0
    # This loop take one name from the list and assigned as i.
    for i in list:
        # Here we check that if the length of the name is more than 5 or not.
        if len(i) >= 5:
            # Here we will be get the numbers of letters inside the name.
            length = len(i)
            # Every time when the loop run it will print the name and the numbers of letters inside that.
            print(i,"length is",length)



# Creating a empty list.
list = []
# Using a for loop we asked the users to input the 5 names.
# Every time when the user input a name it will save the name in name variable.
for i in range(3):
    name = input("Enter the name of the persons  : ")
    # We adding(append) the name in the blank list.
    list.append(name)

# Here we call the search function.
search(list)
