import random
import words
from art import logo, stages
print(logo)
lives = 6
game_over = False
choosen_word = random.choice(words.word_list)
print(choosen_word)
placeholder = ''
for letters in choosen_word:
  placeholder += '_'

print(f"Word to guess: {placeholder}")
correct_letters = []

while not game_over:
  display = ''
  print(f"****************************{lives}/6 LIVES LEFT****************************")
  guss = input("Guess a letter: \n")

  if guss in correct_letters:
    print("You already choosed this letter you lost your live")  
    lives -= 1
  elif guss not in choosen_word:
    print("You choose wrong letter you lost your live")
    lives -= 1

  for letter in choosen_word:
    if letter in correct_letters:
      display += letter
    elif letter == guss:
      display += letter
      correct_letters.append(letter)
    else:
      display += '_'

  print(f"Word to guess: {display}")
  print(stages[lives])
  if lives == 0:
    game_over = True
    print("You lost all your lives \n GAME OVER")
  elif '_' not in display:
    game_over = True
    print("YOU WIN")