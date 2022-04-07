
# Modules
import random
from words import word_list


def choose_difficulty():
    while True:
        difficulty = input("Would you like to play on 'easy' or on 'hard'\n")
        if difficulty.lower() == 'easy':
            starting_lives = 5
            break
        elif difficulty.lower() == "hard":
            starting_lives = 3
            break
        else:
            print("Wrong Input,Try again")
            continue
    return starting_lives


def find_new_word():
    word_to_guess = random.choice(word_list)
    # Uncomment to debug better
    print(word_to_guess)
    anagram_list = list(word_to_guess)
    random.shuffle(anagram_list)
    shuffled_word = ''.join(anagram_list)
    return word_to_guess, shuffled_word


# Starts the Game
def start_game(score):
    lives = choose_difficulty()
    word, anagram = find_new_word()
    print(f"Your current score is {score}")
    global current_score
    # Game Loop
    while lives > 0:
        print(anagram)
        guess = input(f"You have {lives} lives remaining. Guess the word:\n")
        if guess == word:
            print("Congrats You won")
            current_score += 1
            break
        else:
            lives -= 1
            current_score = 0
    # Checks Whether the player lost
    if lives == 0:
        print(f'You run out of lives. The word was {word}\n')


# Game Start
current_score = 0
while True:
    print('Welcome to Anagram Game!')
    start_game(current_score)
    if input("Do you want to play again.Type 'yes' or 'no'\n").lower() == 'no':
        break
