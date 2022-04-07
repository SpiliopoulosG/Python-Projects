from tkinter import *

window =Tk()
window.title("Temperature Unit Converter")
window.minsize(width=750, height=500)

def toCelsius():
    try:
        units_before = int(input_to_change.get())
        units_after = round((units_before - 32) * 5/9)
        result.config(text=f"Your result is {units_after}C")
    except:
        result.config(text="Input must be a whole number")
    result.grid(column=1, row=10)


def toFahrenheit():
    try:
        units_before = int(input_to_change.get())
        units_after = round((units_before * 9/5) + 32)
        result.config(text=f"Your result is {units_after}F")
    except:
        result.config(text="Input must be a whole number")
    result.grid(column=1, row=10)


welcome_message = Label(text="Welcome to Temperature Unit Converter", font=["Arial", 20, "bold"])
welcome_message.grid(column=1, row=2)

result = Label(text=f"Your result is none", font=["Arial", 25, "bold"])

input_to_change = Entry(width=30)
input_to_change.grid(column=1, row=5)

button_to_celsius = Button(text="Convert to Celsius", command=toCelsius, background="#FF9900", width=50)
button_to_celsius.grid(column=0, row=5)
button_to_fahrenheit = Button(text="Convert to Fahrenheit", command=toFahrenheit, background="#FF9900", width=50)
button_to_fahrenheit.grid(column=2, row=5)


window.mainloop()