# Password Generator Project
import random

# Pools
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Starting Code
print("Welcome to the PyPassword Generator!")
letters_to_add = int(input("How many letters would you like in your password?\n"))
symbols_to_add = int(input(f"How many symbols would you like?\n"))
numbers_to_add = int(input(f"How many numbers would you like?\n"))

# Password constant
password = ""

# Password Generator
for let in range(letters_to_add):
    random_index = random.randrange(len(letters))
    password += letters[random_index]
for let in range(numbers_to_add):
    random_index = random.randrange(len(numbers))
    password += numbers[random_index]
for let in range(symbols_to_add):
    random_index = random.randrange(len(symbols))
    password += symbols[random_index]

# Normal Password
# print(f'Your new password is {password}')

# Shuffled Result
shuffled_password = ''.join(random.sample(password, len(password)))
print(f'Your new password shuffled is {shuffled_password}')
