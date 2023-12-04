def sum_to_x(target_integer):
    count = 0
    result = 0

    while count <= target_integer:
        result += count
        count += 1

    return result