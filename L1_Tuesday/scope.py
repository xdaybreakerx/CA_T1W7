# Scope - global and local

fname = "Pat"
lname = "Cummins"

def greet():
    fname = "Steven"
    lname = "Smith"
    print("inside the function")
    print(fname)
    print(lname)
    
    
print("outside the function")
print(fname)
print(lname)
greet()