
# Printing
from art import logo
print(f'{logo}\nWelcome to Secret Auction')

# Starting Constants
list_of_players = []
p_values = {}

# Starting Loop
while True:
    name = input("What's the name of the person?\n")
    bid = int(input("What is the bid amount?\n"))
    p_values[name] = bid
    end = input("Is there another player? Yes or No?\n")
    if end.lower == 'yes':
        continue
    elif end.lower() == 'no':
        break

# End of Game Count
current_winner = ""
current_price = 0
max_price = 0
for value in p_values:
    current_price = p_values[value]
    if max_price < current_price:
        max_price = current_price
        current_winner = value
    else:
        continue

# Prints Winner
print(f"The winner is {current_winner} with the winning bid of {max_price}")
