import turtle
import pandas

# CONSTANT
BACKGROUND_IMAGE = "blank_states_img.gif"
STATES_FOUND = 0
FONT = ('Courier', 10, "normal")

# Making of the Screen
screen = turtle.Screen()
screen.title("U.S State Game")
screen.addshape(BACKGROUND_IMAGE)
turtle.shape(BACKGROUND_IMAGE)
state_text = turtle.Turtle()


# Make everything inside a list lowercase
def makes_lowercase(list_to_lower):

    list_length = len(list_to_lower)
    for i in range(0, list_length):
        list_to_lower[i] = list_to_lower[i].lower()
    return list_to_lower


def go_to_location(state):

    state_before_capitalization = state.split()
    for i in range(0, len(state_before_capitalization)):
        state_before_capitalization[i] = state_before_capitalization[i].capitalize()
    state_after_capitalization = ' '.join(state_before_capitalization)
    state_information = file[file.state == state_after_capitalization]

    state_text.penup()
    state_text.hideturtle()
    state_text.goto(int(state_information.x), int(state_information.y))
    state_text.write(f"{state_after_capitalization}", font=FONT)


# Preparing data
file = pandas.read_csv("50_states.csv")
states_list = file["state"].to_list()
states_list = makes_lowercase(states_list)
found_states_list = []


while states_list is not []:

    answer_state = screen.textinput(title=f"{STATES_FOUND}/50 States Correct",
                                    prompt="What's another state's name?")

    if answer_state.lower() in states_list:
        STATES_FOUND += 1
        states_list.remove(f'{answer_state.lower()}')
        found_states_list.append(f'{answer_state.capitalize()}')
        go_to_location(answer_state)

    if answer_state.lower() == "exit":

        study_material = pandas.DataFrame(states_list)
        study_material.to_csv("States_to_study.csv")
        exit()

if states_list is []:
    print("Congrats, You found them all!")


screen.mainloop()
