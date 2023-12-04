def string_filter(list_of_words):

    result = []

    for word in list_of_words:
        if word in ["heck", "dang"]:
            continue

        result.append(word)


    return result