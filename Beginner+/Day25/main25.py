import pandas

file = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in file.iterrows()}
# print(phonetic_dict)

# Create a list of the phonetic code words from a word that the user inputs.
while True:
    try:
        letters_in_word = []
        for letter in input("Tell me a word to spell with examples:\n").upper():
            letters_in_word.append(phonetic_dict[letter])
        print(letters_in_word)
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please.")