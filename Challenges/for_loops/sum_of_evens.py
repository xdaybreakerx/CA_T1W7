def sum_of_evens(input_list):
    result = 0
    
    for input in input_list:
        if input % 2 == 0:
            result += input
        else:
            continue

    return result