import art
print(art.logo)
from data import data
import random

score = 0
account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
  account_b = random.choice(data)


def formate_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]

  print(f"{account_name} a {account_descr} from {account_country}")

def chedck_answer(user_guess, a_followrs, b_followers):
  if a_followrs > b_followers:
    return user_guess == "a"
  else:
    return user_guess == "b"

print(f"Compare A: {formate_data(account_a)}")
print(art.vs)
print(f"Compare B: {formate_data(account_b)}")

guess = input("Who has more followers? Type 'A' or 'B'")

a_followr_count = account_a["follower_count"]
b_followr_count = account_b["followr_count"]

is_correct = chedck_answer(guess, a_followr_count, b_followr_count)

if is_correct:
  score += 1
  print(f"You're right! Current score {score}")
else:
  print("Sorry, that's wrong. Final score: {score}")