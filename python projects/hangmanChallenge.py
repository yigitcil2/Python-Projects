print("Welcome to the game! \n "
      "You will need to guess the letters of a random choiced word from the word list")
wordList = ["attack", "scan", "hacker"]

import random

theWord = random.choice(wordList)
print(theWord)
displayWord = []
print("You have 5 guesses")
for letter in theWord:
    displayWord += "_"

print(displayWord)

num = 0
game_over = False
while not game_over:
    guess = input("Guess a letter").lower()
    for position in range(len(theWord)):
        letter = theWord[position]
        if letter == guess:
            displayWord[position] = letter
    if guess not in theWord:
        num += 1
        guessesLeft = 5 - num
        print(f"You have {guessesLeft} guesses left")
        if num >= 5:
            print("You Lose")
            game_over = True

    print(displayWord)

    if "_" not in displayWord:
        print("You win")
        game_over = True







