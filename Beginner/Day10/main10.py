
import random

while True:
    print("Welcome to number Guessing Game!\nI am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty.Type 'easy' or 'hard':").lower()
    if difficulty == 'easy':
        total_lives = 10
    elif difficulty == 'hard':
        total_lives = 5
    print(f"You have {total_lives} attempts remaining to guess the number")

    # Number Thought
    number = random.randrange(0, 100)

    # Uncomment to show you the solution
    # print(f"Psst the number is {number}")

    # Guess
    while total_lives != 0:
        guess = int(input('Make a guess: '))
        if guess > number:
            print('Too high.\nGuess again.')
            total_lives -= 1
            print(f"You have {total_lives} attempts remaining to guess the number")
        elif guess < number:
            print('Too low.\nGuess again.')
            total_lives -= 1
            print(f"You have {total_lives} attempts remaining to guess the number")
        elif guess == number:
            print(f"You got it the answer was {number}!")
            break

    if total_lives == 0:
        print(f'You lost,the number was {number}')
    if input("Do you want to play again 'yes' or 'no':").lower() == "no":
        break
