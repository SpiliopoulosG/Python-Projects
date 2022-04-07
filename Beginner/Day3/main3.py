
# Logo
logo = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

# Starting Dialog
print(f'{logo}\nWelcome to Treasure Island.\nYour mission is to find the treasure.')
# Story Cycle
print("You see a small pond in front of you !\n")
# First Choice
choice_1 = input('Do you jump in the waters or wait? jump or wait ? \n')
if choice_1.lower() == 'wait':
    print("You waited for 3 hours and nothing happened so you left!")
elif choice_1.lower() == "jump":
    print('You jumped in and a world of fishes and sea life was unveiled to you! You see 2 big caves,one in the left'
          ' and one in the right')
    choice_2 = input('Where do you go left or right ?\n')
    # Second Choice
    if choice_2.lower() == 'left':
        print('You entered and withing seconds you felt an evil presence behind you, You had just turned around when'
              ' a big monster appeared out of nowhere and ate your head\nGame Over!')
    elif choice_2.lower() == 'right':
        print('You swim and swim and swim and you exit the cave and in front of you a giant city unfolds!There are 3'
              ' main building ahead of you,a Church ,a Tavern and a Castle')
        choice_3 = input('Where do you enter,The Church,The Tavern or The  Castle\n')
        # Third Choice
        if choice_3.lower() == 'the church':
            print("You entered the Church and a huge Spider fell out of the church's sealing, not even God could save "
                  "you from the spider\nGame Over!")
        elif choice_3.lower() == 'the tavern':
            print("You entered the Tavern and it was full of extremely powerful drunk people, You couldn't even take "
                  "a step before someone grabbed you and snapped your neck!\nGame Over!")
        elif choice_3.lower() == 'the castle':
            print("A huge golden statue and thousand of coins appear in front of you, congratulations you found the "
                  "Treasure\nYou Win!")
    else:
        print('Wrong Choice, you forgot that you were in the water so you drown cause you waited too much time')
