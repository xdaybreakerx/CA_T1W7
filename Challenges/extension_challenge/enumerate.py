def threeven(some_list):
    
    for index, number in enumerate(some_list):
            if number % 3 == 0:
                return index
    return None
            
threeven([5, 6, 7, 8, 9])