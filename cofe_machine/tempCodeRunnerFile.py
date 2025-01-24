from main import resources
from main import menu
Profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

is_on = True

while is_on:
    choice = input("What would you like? (esspresso/latte/cappuccino)")
    if choice == "off":
       is_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${Profit}")
    else: 
        drink = menu[choice]
        print(drink)