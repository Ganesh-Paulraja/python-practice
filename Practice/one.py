import random

print("ROCK, PAPER, SCISSOR")

options = {
    "Rock": '''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''',
    "Paper": '''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            ''',
    "Scissors": '''
                _______
            ---'   ____)____
                      ______)
                  __________)
                  (____)
            ---.__(___)
            '''
    
}
option_map = list(options.keys())

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer_choice = random.randint(0,2)

print('your choice:')
print(options[option_map[choice]])

print('computer choice:')
print(options[option_map[computer_choice]])

# if choice == computer_choice:
#     print("It's a draw")
# elif choice == 0 and computer_choice == 1:
#     print("You Failed")
# elif choice == 0 and computer_choice == 2:
#     print("You Win!")
# elif choice == 1 and computer_choice == 0:
#     print("You Win!")
# elif choice == 1 and computer_choice == 2:
#     print("You Failed")
# elif choice == 2 and computer_choice == 0:
#     print("You Failed")
# elif choice == 2 and computer_choice == 1:
#     print("You Win!")

winning_chances = ((0, 2), (1, 0), (2, 1))

if choice == computer_choice:
    print("It's a draw")
elif (choice, computer_choice) in winning_chances:
    print("You Win!")
else: 
    print("You Failed")