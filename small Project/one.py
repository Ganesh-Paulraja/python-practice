image = '''*******************************************************************************
|                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
|                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
|           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************'''

print(image)
print('Welcome to Treasure Island. \n Your mission is to find the treasure.')
option = input('''You're at a crossroad, where do you want to go? Type "left" or "right": ''').lower

if option == 'left':
    option = input('''you've come to a lake, there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.: ''').lower()
    if option == 'wait':
        option = input('''You arrive at the island unharmed.There is house with 3 doors. One "red", one "yellow" and one "blue". Which color do you choose: ''').lower
        if option == 'red':
            print("It's room full of fire. Game Over.")
        elif option == 'yellow':
            print('You found the treasure. You Win!')
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print('you got attacked by an angry trout. Game Over.')
        
else: 
    print('You fell in to a whole. Game Over.')