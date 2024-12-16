import random
import art
from data import data

game_Over = False

def random_val ():
  return random.choice(data)

random_value = random_val ()
random_value_2 = random_val ()
score = 0
print(art.logo)

while not game_Over:
  print(f'Compare A: {random_value['name']}, a {random_value['description']}, from {random_value['country']}')
  print(art.vs)
  print(f'Against B: {random_value_2['name']}, a {random_value_2['description']}, from {random_value_2['country']}')
  option_value = input("Who has more followers? Type 'A' or 'B': ").lower()
  print(art.logo)
  if random_value['follower_count'] > random_value_2['follower_count'] and option_value == 'a':
    score += 1
    print(f"You're right! Current score {score}")
    random_value_2 = random_val()
  elif random_value['follower_count'] < random_value_2['follower_count']  and option_value == 'b':
    score += 1
    print(f"You're right! Current score {score}")
    random_value = random_value_2
    random_value_2 = random_val()
  else:
    game_Over = True
    print(f"Sorry, that's wrong. Final score: {score}.")