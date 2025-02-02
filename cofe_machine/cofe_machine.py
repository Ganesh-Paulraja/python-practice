from main import resources
from main import menu
Profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins insered"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total



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
        # we can call functions like this also
        if is_resource_sufficient(drink["ingredients"]):
            process_coins()
        
 