def sum_to_x(target_integer):
    result = 0
    for i in range(1, target_integer + 1):
        result += i
        i += 1

    return result