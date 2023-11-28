# if a number is prime or not

def is_prime(number):
    for i in range(2, number):
        if (number % i == 0):
            print("Not a Prime")
            break
    else:
        print("A Prime")

is_prime(5)
is_prime(55)
is_prime(12)
is_prime(29)
is_prime(34)
is_prime(37)