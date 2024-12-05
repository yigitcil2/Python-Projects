import random
import art_blackjack
def get_card():
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # king, quen, joker...
    card = random.choice(card_list)
    return card


def calculate_score(list_of_cards):
    score = 0
    for i in list_of_cards:
        score += i
    if score == 21 and len(list_of_cards) == 2:
        return 0
    elif score < 21:
        return score

    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return score

def compare(u_score, computer_score):
    if u_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win"
    elif u_score > 21:
        return "Went over. Lose"
    elif computer_score > 21:
        return "Opponent went over, You Win"
    elif u_score > computer_score:
        return"You win"
    elif u_score < computer_score:
        return "You lose"


def play_game():
    print(art_blackjack.blackjack_logo)
    user_cards = []
    npc_cards = []
    game_ends = False
    npc_cards.append(get_card())
    for _ in range(2):
        new_card = get_card()
        user_cards.append(new_card)
    while game_ends == False:
        user_score = calculate_score(user_cards)
        npc_score = calculate_score(npc_cards)

        print(f"Your cards: {user_cards}, and your score: {user_score}")
        print(f"Computer's first card: {npc_cards[0]}")

        if user_score == 0 or npc_score == 0 or user_score > 21:
            game_ends = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == 'y':
                user_cards.append(get_card())
            else:
                game_ends = True
    while npc_score != 0 and npc_score < 17: 
        npc_cards.append(get_card())
        npc_score = calculate_score(npc_cards)

    print(f"Your final hand {user_cards} and final score: {user_score}")
    print(f"Computere's final hand {npc_cards} and final score: {npc_score}")
    print(compare(user_score,npc_score))

while input ("Do you want to continue playing Blackjack? 'y' or 'n': ") == 'y':
    print("\n "* 20)
    play_game()