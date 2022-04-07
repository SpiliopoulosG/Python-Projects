
# Blackjack
import random
from art import logo
print(logo)

# Starting Constants
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Computer

def draw_card():
    return random.choice(cards)


def count_card(card_list):
    total = 0
    for i in card_list:
        total += i
    return total


def who_won(p_total, c_total):
    # Winning Conditions Checker
    if p_total > 21:
        return False
    elif c_total > 21:
        return True
    elif p_total > c_total:
        return True
    elif p_total < c_total:
        return False


# Start of Game
while True:
    shall_play = input("Do you want to play a game of Blackjack? Type 'yes' or 'no':\n").lower()
    if shall_play == 'yes':

        # Computer
        computer_hand = []
        while True:
            computer_hand.append(draw_card())
            if count_card(computer_hand) > 16:
                break
            if count_card(computer_hand) > 21:
                break

        # Player Time
        player_hand = []
        player_hand.append(draw_card())
        print(f"Computer's first card is {computer_hand[0]}")
        while True:
            print(player_hand)
            another_card = input("Do you want another card? Type 'yes' or 'no':\n")
            if another_card.lower() == "yes":
                player_hand.append(draw_card())
                if count_card(player_hand) > 21:
                    print(player_hand)
                    print("You went over 21.")
                    break
            elif another_card.lower() == "no":
                break

        # Checks who won
        player_total = count_card(player_hand)
        computer_total = count_card(computer_hand)
        if who_won(player_total, computer_total) is True:
            print(f"You won!You had a total of {player_total} and computer had {computer_total}")
        if who_won(player_total, computer_total) is False:
            print(f"You Lost!You had a total of {player_total} and computer had {computer_total}")
    elif shall_play == 'no':
        break

print('Maybe Next time')
