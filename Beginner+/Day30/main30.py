
import json
from tkinter import *
from tkinter import messagebox
import pandas
import random
import time

# ---------------------------- CONSTANTS ------------------------------- #

BLACK = "#3A3845"
WHITE = "#FDF6EC"
LIGHT_BLUE = "#B1DDC6"
FONT_NAME = "Roboto"
current_card = None
unknown_cards = []
known_cards = []

# ---------------------------- Data Section ------------------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    data = data.to_dict(orient="records")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/french_words.csv")
    data = data.to_dict(orient="records")


# ---------------------------- Next Card ------------------------------- #
def next_card():
    global current_card, timer
    window.after_cancel(timer)
    while len(known_cards) < len(data):
        current_card = random.choice(data)
        if current_card in known_cards:
            pass
        else:
            break
    if len(known_cards) == len(data):
        return messagebox.showinfo(title=f"Cards", message="You have finished all the cards.")
    canvas.itemconfig(background_image, image=front_card)
    canvas.itemconfig(title, text="French", fill=BLACK)
    canvas.itemconfig(word_to_guess, text=f"{current_card['French']}", fill=BLACK)

    timer = window.after(3000, func=show_answer)


# ---------------------------- Show Answer ------------------------------- #
def show_answer():
    canvas.itemconfig(background_image, image=back_card)
    canvas.itemconfig(title, text="English", fill=WHITE)
    canvas.itemconfig(word_to_guess, text=f"{current_card['English']}", fill=WHITE)


# ---------------------------- Right ------------------------------- #
def right():
    if current_card not in known_cards:
        known_cards.append(current_card)
    next_card()


# ---------------------------- Wrong ------------------------------- #
def wrong():
    if current_card not in unknown_cards:
        unknown_cards.append(current_card)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.minsize(height=500, width=500)
window.config(padx=50, pady=50, bg=LIGHT_BLUE)

timer = window.after(3000, func=show_answer)

canvas = Canvas(width=801, height=527, bg=LIGHT_BLUE, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
background_image = canvas.create_image(400, 264, image=front_card)
title = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
word_to_guess = canvas.create_text(400, 264, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0,columnspan=2, row=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=right)
right_button.grid(column=0, row=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, bg=LIGHT_BLUE, command=wrong)
wrong_button.grid(column=1, row=2)

next_card()

window.mainloop()

try:
    remaining_words_to_learn = pandas.DataFrame(unknown_cards)
    remaining_words_to_learn.to_csv("data/words_to_learn.csv", index=False)
except:
    pass
