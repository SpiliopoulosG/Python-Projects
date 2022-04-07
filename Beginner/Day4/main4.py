# Modules
import random

# Images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Getting down the parameters
pool = ["rock", "paper", "scissors"]
player_choice = input("What do you choose? Type rock, paper or scissors.\n")
computer_choice = random.choice(pool)

# Uncomment in if you want to see the choice
# print(choice_choice, computer_choice)

# Game Logic
# Rock
if player_choice.lower() == "rock":
    print(rock)
    if computer_choice == "rock":
        print('Computer chose:\n' + rock + "\nIt's a Tie\n")
    elif computer_choice == "paper":
        print('Computer chose:\n' + paper + "\nYou Lose\n")
    elif computer_choice == "scissors":
        print('Computer chose:\n' + scissors + "\nYou win\n")
# Paper
elif player_choice.lower() == "paper":
    print(paper)
    if computer_choice == 'rock':
        print('Computer chose:\n' + rock + "\nYou Win\n")
    elif computer_choice == 'paper':
        print('Computer chose:\n' + paper + "\nIt's a Tie\n")
    elif computer_choice == 'scissors':
        print('Computer chose:\n' + scissors + "\nYou Lose\n")
# Scissors
elif player_choice.lower() == "scissors":
    print(scissors)
    if computer_choice == 'rock':
        print('Computer chose:\n' + rock + "\nYou Lose\n")
    elif computer_choice == 'paper':
        print('Computer chose:\n' + paper + "\nYou Win\n")
    elif computer_choice == 'scissors':
        print('Computer chose:\n' + scissors + "\nIt's a Tie\n")
