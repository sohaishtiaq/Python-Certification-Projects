menu = {
    'pizza' : 500,
    'burger' : 400,
    'fries' : 200,
    'loaded_Fries' : 750,
    'wraps' : 450,
    'Fried_Chicken' : 250
}

print("Welcome to Soha's Food Bar")
print("pizza : 500\nburger : 400\nfries : 200\nloaded_Fries : 750\nwraps : 450\nFried_Chicken : 250")

order_total = 0

item_1 = input("Enter from menu what you want = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to the order")
else:
    print(f"ordered item {item_1} is not available yet")

another_order = input("Do you want to order anything else? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter from menu what you want = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to the order")
    else:
        print(f"ordered item {item_2} is not available yet")

print(f"The total amount to pay is {order_total}") 
