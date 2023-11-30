# pseudo code example:

# Input numerator as n, and denominator as d

# if d == 0
#    display "Denominator cannot be 0" as output

# else
#    q = n / d
#    display q

n = int(input("Enter numerator: "))
d = int(input("Enter denominator: "))

if d == 0: 
    print("Denominator cannot be 0")
else:
    q = n / d
    print(q)