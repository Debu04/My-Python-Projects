'''
This code is used to print the below assignment
'''


# Save the values in the variable
x = "ABCD"
y = "PQR"

# Using a For loop to run the code 4 times
for i in range(4):
    # Code always start from right to left
    # So first it print the y variable
    # y[i:] it means that we fetching the values of y and it start for i(4) to end to y values
    # Then it print x variable(x[:i+1] it means that it starts from start to the i(4th value) of x)
    # In every loop it replace the y values with x and print it
    print(x[:i+1]+y[i:])


# Results

#           APQR
#           ABQR
#           ABCR
#           ABCD
