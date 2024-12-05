import random

selection = input("What do you choose? \nRock: 0\nPaper: 1 \nScissors: 2")
list = ["Rock", "Paper", "Scissors"]

npc_choice = random.choice(list)


if selection == '0':

    if npc_choice == list[0]:
        print("It's a draw")
    elif npc_choice == list[1]:
        print("You lose")
    elif npc_choice == list[2]:
        print("You win")
elif selection == '1':
    if npc_choice == list[0]:
        print("You win")
    elif npc_choice == list[1]:
        print("It's a draw")
    elif npc_choice == list[2]:
        print("You lose")
elif selection == '2':
    if npc_choice == list[0]:
        print("You lose")
    elif npc_choice == list[1]:
        print("You win")
    elif npc_choice == list[2]:
        print("It's a draw")