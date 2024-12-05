#Hangman
import random
from hangmanStages import stages, logo
from hangmanWords import word_list

print(logo)

generated_word = random.choice(word_list)
print(generated_word)

placeholder = ""
for i in generated_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

player_lives = 6

while game_over == False:
    print(f"You have {player_lives} lives ")
    user_guess = input("guess for letter").lower()

    if user_guess in correct_letters:
        print(f"You have already guessed {user_guess}")

    display = ""
    for letter in generated_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(user_guess)
        elif letter in correct_letters:
            display += letter
        elif letter != user_guess:
            display += "_"

    print(display)

    if user_guess not in generated_word:
        player_lives = player_lives - 1
        print(f"You guessed wrong, {player_lives} lives left")
        if player_lives == 0:
            game_over = True
            print("You lose")
    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[player_lives])
