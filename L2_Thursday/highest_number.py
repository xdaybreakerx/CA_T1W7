# pseudo code example:

# Take 3 numbers as a, b, and c as input from the user

# if a > b:
    # if a > c:
    # print a
    # else:
    # print c

# else:
    # if b > c:
    # print b
    # else: 
    # print c
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b: 
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else: 
        print(c)