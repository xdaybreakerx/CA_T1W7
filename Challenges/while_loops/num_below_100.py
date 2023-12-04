def input_within_range():
    min_value = 1
    max_value = 100

    user_input = 0

    while user_input < min_value or user_input > max_value:
        user_input = int(input("Please enter a number between 1 and 100: "))
        if user_input < min_value: 
            print("ERROR: below min value")
        elif user_input > max_value:
            print("ERROR: above max value")
        
    return user_input