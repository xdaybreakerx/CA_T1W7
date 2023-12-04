LIST_OF_WORDS = [
    "serendipity",
    "petrichor",
    "supine", 
    "solitude",
    "aurora",
    "idyllic",
    "clinomania",
    "pluviophile",
    "euphoria",
    "sequoia"
]

def filter_list(some_string): 
    output_list = []

    for word in LIST_OF_WORDS:
        if some_string in word:
            output_list.append(word)
        else:
            continue 

    return output_list