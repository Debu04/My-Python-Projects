''' Here we taking three values from the user
    and find the greatest number from them
'''


# Taking the input from the user
a = int(input("First number : "))
b = int(input("Second number : "))
c = int(input("Third number : "))

# If a is greater then b . Then we compare a with c that who is greater.
if a > b:
    if a > c:
        print("First is greatest number",a)
    else:
        print("Third is greatest number",c)

# If b is greater then a . Then we compare b with c that who is greater.
if b > a:
    if b > c:
        print("First is greatest number",b)
    else:
        print("Third is greatest number",c)
