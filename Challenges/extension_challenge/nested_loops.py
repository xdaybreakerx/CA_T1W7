def count_the_cs(some_list):
    result = 0

    for string in some_list:
        for char in string:
            if char == "c" or char == "C":
                result += 1

    return result