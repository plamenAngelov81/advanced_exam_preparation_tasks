def shop_from_grocery_list(*args):
    items = [x for x in args]
    budget = items.pop(0)
    grocery_list = items.pop(0)
    client_list = []
    for product_data in items:
        product = product_data[0]
        price = product_data[1]
        if product in grocery_list and product not in client_list:
            if budget >= price:
                client_list.append(product)
                budget -= price
                grocery_list.remove(product)
            else:
                break

    if len(grocery_list) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result = f'You did not buy all the products. Missing products: {", ".join(x for x in grocery_list)}.'
        return result


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))