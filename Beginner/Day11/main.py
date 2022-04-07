# Start
import random
from art import vs
from art import logo
from game_data import data

# Pick an index from the data to compare
def pick():
    num = random.randint(0, len(data) - 1)
    return data[num]['name'], data[num]['description'], data[num]['country'], data[num]["follower_count"]


# Compares the follower of the one index to the followers of the other
def compare(followers_of_one, followers_of_other):
    if followers_of_one > followers_of_other:
        return "A"
    else:
        return "B"


# Game Logic
print(logo)
while True:
    score = 0
    A_name, A_description, A_country, A_followers = pick()
    B_name, B_description, B_country, B_followers = pick()
    while True:
        print(f"Current Score:{score}\n"
              f"Compare A: {A_name}, a {A_description}, from {A_country}\n"
              f"{vs}\n"
              f"To B: {B_name}, a {B_description}, from {B_country}")

        guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess.upper() == compare(A_followers, B_followers):
            score += 1
            if guess.upper() == "B":
                A_name, A_description, A_country, A_followers = B_name, B_description, B_country, B_followers
            B_name, B_description, B_country, B_followers = pick()
        else:
            print(f"You lost. Your score was {score}")
            break
    if input("Do you want to play again: Type 'yes' or 'no'").lower() == "no":
        break

