
'''
This code is used to sort the Array in Ascending order

Here we first run the two For loop and compare the values from the Loops one by one
At a time both of the loops is picking one numbers and we compare them.

The first For loop is starting from 0 to the lenth of the vals.
But the second Loop is starting from 0 to the lenth-1 (That is 2nd last value of vals)

Every programme is starts from right to left.
'''

print("Results in manual methord")
from array import *
vals = array("i",[1,8,9,3,5])
# This Loop is star from 0 and ends last value of vals.
for i in range(len(vals)):
    # But this Loop is star from 0 and ends the 2nd last value of vals.
    for j in range(len(vals)-1):
        if vals[j] > vals[j+1]:
            temp = vals[j+1]
            vals[j+1] = vals[j]
            vals[j] = temp
            # After shorting the old values is replaced by the new values.
            print(vals)


# Or Sorting using inbuilt function
print("Result using inbuilt function")

print(sorted(vals))

