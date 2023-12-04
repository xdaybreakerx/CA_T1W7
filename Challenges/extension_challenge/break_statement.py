def shopping_list():
    prompt_phrase = ("Enter an item to add to your shopping list. (Enter 'quit' to end.): ")
    item_list = []

    while True:
        user_input = input(prompt_phrase)

        if user_input == "quit":
            break
        else:
            item_list.append(user_input)

    return item_list