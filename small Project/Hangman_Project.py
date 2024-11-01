import random
word_list = ["aardvark", "baboon", "camel"]

lives = 6
game_over= False

chosen_word = random.choice(word_list)
print(chosen_word)

pleaceholder = ""
for letter in chosen_word:
    pleaceholder += '_'

print("Word to guess " + pleaceholder)

correct_letters = []

# while not game_over:
    print("*****************************{lives}/6 LIVES LEFT*************************")