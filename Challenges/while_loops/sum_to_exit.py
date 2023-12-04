def sum_of_inputs():
    total = 0
    user_input = 0

    while user_input !="end":
        total += int(user_input)
        user_input = input("Enter a number: ")

    return total