def update_warehouse_product_database():
    warehouse_product_database = {
        "Xbox": 77,
        "PS5": 912,
        "Switch": 311,
        "Steam Deck": 51,
        "Valve Index": 102
    }
    todays_orders = {
        "Xbox": 12,
        "PS5": 112,
        "Switch": 310,
        "Steam Deck": 51,
        "Valve Index": 62
    }

    # Update warehouse_product_database based on todays_orders
    for product, ordered_quantity in todays_orders.items():
        warehouse_product_database[product] -= ordered_quantity
        warehouse_product_database[product] = max(warehouse_product_database[product], 0)

    return warehouse_product_database