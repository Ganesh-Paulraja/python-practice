from art import logo
import random

print(logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")

def number_check ():
    chosen_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    lives = 0
    lives = 10 if difficulty == "easy" else 5
    print(f"You have {lives} attempts remaining to guess the number.")

    game_over = False

    while not game_over:
        num = int(input("Guess the number: "))

        if num > chosen_number:
            lives -= 1
            print(f"Too Big \n You have {lives} attempts remaining to guess the number.")
        elif num == chosen_number:
            game_over = True
            print("You Found it. You win!") 
        else:
            lives -= 1
            print(f"Too Low \n You have {lives} attempts remaining to guess the number.")
        
        if lives == 0:
          game_over = True
          print("0 lives left you lost")
          return

number_check ()   