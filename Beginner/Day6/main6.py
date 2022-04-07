
# HangMan

import random
from hangman_art import stages

# Getting the list
from hangman_words import word_list

# Word Selection
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Starting Constants
end_of_game = False
lives = 6

# Logo
from hangman_art import logo

print(logo)

# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Start of Loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    guess_list = []

    for position in display:
        if position == guess:
            print(f'You have already entered {guess} ,please enter another one')

    # Checks guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Checks if user is wrong.
    if guess not in chosen_word and guess not in guess_list:
        if guess not in guess_list:
            guess_list.append(guess)
        print(f"The letter '{guess}' is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nThe word was {chosen_word}")

    # Checks if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
