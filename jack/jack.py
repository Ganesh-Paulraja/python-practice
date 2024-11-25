from art import logo
import random

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_game = True

def draw(user_val, comp_card_2 , comp_cards):
   global continue_game 
   print(f"Your final hand: {user_val}")
   comp_cards.append(comp_card_2)
   print(f"Computer's final hand: {comp_cards}")
   print("Game Draw")
   continue_game = False

def win(user_val, comp_card_2, comp_cards):
   global continue_game 
   print(f"Your final hand: {user_val}")
   comp_cards.append(comp_card_2)
   print(f"Computer's final hand: {comp_cards}")
   print("Game Win")
   continue_game = False

def lose(user_val, comp_card_2, comp_cards):
   global continue_game 
   print(f"Your final hand: {user_val}")
   comp_cards.append(comp_card_2)
   print(f"Computer's final hand: {comp_cards}")
   print("You Lose")
   continue_game = False

if play == 'y':
    user_card_1 = random.choice(cards)
    user_card_2 = random.choice(cards)
    computer_card_1 = random.choice(cards)
    computer_card_2 = random.choice(cards)

    user_cards = [user_card_1, user_card_2]
    computer_cards = [computer_card_1]

    while continue_game:
      user_score = sum(user_cards)
      computer_score = sum(computer_cards) + computer_card_2
      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"Computer's first card: {computer_cards}")
      if user_score == 21 and computer_score == 21:
         draw(user_cards, computer_card_2, computer_cards)
      elif user_score > 21:
        if 11 in user_cards:
           user_score = user_score - 10
        else:
           lose(user_cards, computer_card_2, computer_cards)
      elif computer_score > 21:
         if 11 in computer_cards:
            computer_score = computer_score - 10
         else:
           win(user_cards, computer_card_2, computer_cards)
      elif user_score == 21:
          win(user_cards, computer_card_2, computer_cards)
      elif computer_score == 21:
         lose(user_cards, computer_card_2, computer_cards)
      else:
        add_more = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if add_more == 'y':
            new_user_card = random.choice(cards)
            user_cards.append(new_user_card)
            if computer_score < 17:
                new_computer_card = random.choice(cards)
                computer_cards.append(new_computer_card)
        else: 
            if user_score == computer_score:
              draw(user_cards, computer_card_2, computer_cards)
            elif user_score > computer_score:
              win(user_cards, computer_card_2, computer_cards)
            else:
              lose(user_cards, computer_card_2, computer_cards)
      

    
    

   

    