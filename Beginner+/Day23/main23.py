
PLACEHOLDER = "[name]"
name_list = []
# Opens a file and take each line out of it and appends to a list
with open(r".\Input\Names\invited_names.txt",
          mode='r') as file:
    for line in file:

        name_list.append(line.rstrip("\n"))

# Opens the starting file which we will read from the starting script
with open(r".\Input\Letters\starting_letter.txt",
               mode ='rt') as letter_file:
    letter_contents = letter_file.read()
    # Looping through items in the list
    for name in name_list:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        # Creates and write the end file
        with open(fr".\Output\ReadyToSend\{name}.txt",
               mode ='wt') as completed:
            completed.write(new_letter)
