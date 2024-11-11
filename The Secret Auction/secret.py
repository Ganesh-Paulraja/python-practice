from art import logo

print(logo)

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

continue_bidding = True
user_bids = {}

while continue_bidding:
  user_name = input("What is your name?")
  user_bid = float(input("What is your bid?"))
  user_repeat = input("Are there any other bidders? Type 'Yes or No'").lower()
  user_bids[user_name] = user_bid
  if user_repeat == 'yes':
    print('\n' * 5)
  else:
    continue_bidding = False
    find_highest_bidder(user_bids)