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
    "scissors": '''
                _______
            ---'   ____)____
                      ______)
                  __________)
                  (____)
            ---.__(___)
            '''
    
}

# choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 3 for Scissors")

keys = list(options.keys())

# print(options[keys[0]])

computer_choice = random.randint(0,2)

print(computer_choice)