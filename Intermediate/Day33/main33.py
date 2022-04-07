import json
from tkinter import *
import requests

def get_quote():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = response.json()
    canvas.itemconfig(quote_text, text=f"{joke['value']}", font=("Arial", 20, "bold"))


window = Tk()
window.title("Chuck Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=552)
background_img = PhotoImage(file="background_large.png")
canvas.create_image(200, 276, image=background_img)
quote_text = canvas.create_text(200, 247, text="Chuck Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="chuck.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()