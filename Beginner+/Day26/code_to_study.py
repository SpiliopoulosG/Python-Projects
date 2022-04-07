from tkinter import *

window = Tk()
window.title("Temperature Unit Converter")
window.minsize(width=500, height=400)

def button_clicked():
    my_label.config(text=f"{input.get()}")
    print(input.get())

# Label
# Step 1 Create Component
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))

# Step 2 Place Container
my_label.pack()

# Step 3 Change Properties
# my_label.config(text="New Text")

# Button
button = Button(text="Click me", command=button_clicked)
button.pack()

# Input

input = Entry(width=25)
input.pack()



window.mainloop()