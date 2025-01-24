from main import resources
from main import menu

is_on = True
profit = 0

while is_on:
    choice = input("What would you like? (esspresso/latte/cappuccino)\n")

    if choice == "off":
        is_on = False
    
