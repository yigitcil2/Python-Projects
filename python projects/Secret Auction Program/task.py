#print("\n" * 100)

user_dictionary = {}
if_continue = True
while if_continue == True:
    user_name = input("Enter your name: ")

    bid = int(input("Enter the bid: $"))

    user_dictionary[user_name] = bid

    if_continue_input = input("'yes' for continue, 'no' for stop")
    if if_continue_input == "yes":
        if_continue = True
    elif if_continue_input == "no":
        if_continue = False

print(user_dictionary)


def find_winner(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for key in user_dictionary:
        bid_amount = bidding_dictionary[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The winner is {winner} with the bid of {highest_bid}")
find_winner(user_dictionary)
