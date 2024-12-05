import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print("Welcome to the game")

print("Try to guess the number selected between 1 and 100.")
random_number = random.randint(0,100)

def choose_difficulty():
    game_difficulty = input("Choose a difficulty. 'easy' or ' hard' ")
    if game_difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif game_difficulty == "hard":
        return HARD_LEVEL_TURNS

def check(user_guess, the_goal):
    if user_guess > the_goal:
        print("Too high")
    elif user_guess < the_goal:
        print("Too low")
    else:
        print(f"You found the answer. {the_goal}")

guess = int(input("Guess the number"))
lives = choose_difficulty()
 

