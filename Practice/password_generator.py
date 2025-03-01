import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '^', '&', '*', '(', ')']

user_letters = int(input('How many letters you want?\n'))
user_numbers = int(input("How many numbers you want?\n"))
user_symbols = int(input("How many symbols you want?\n"))

password = []

for i in range(0, user_letters):
    password.append(random.choice(letters))

for i in range(0, user_numbers):
    password.append(random.choice(numbers))

for i in range(0, user_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
print(password)

user_passwordl = ''.join(password)
print(user_passwordl)