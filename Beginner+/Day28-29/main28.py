import json
from tkinter import *
from tkinter import messagebox
# import pandas
import pyperclip
# ---------------------------- CONSTANTS ------------------------------- #
LIGHT_BLUE = "#95D1CC"
RED = "#C74B50"
WHITE = "#FDF6EC"
FONT_NAME = "Roboto"

# ---------------------------- Search Function ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading Data
            data = json.load(data_file)
            try:
                return messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']} ")
            except KeyError:
                return messagebox.showerror(title="Error", message=f"No Details for {website} exist")
    except FileNotFoundError:
        return messagebox.showerror(title="Error", message=f"No Data File Found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_connection_information():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        return messagebox.showerror(title="Error", message="You left a space empty.Enter valid input")

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered: \nEmail: {email_username} "
                                                  f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:

        # Panda Way

        # file_values = {"Website": [website],
        #                "Email-Username": [email_username],
        #                "Password": [password],
        #                }

        # If file doesn't exist
        # password_manager_file.to_csv("password_manager_file.csv", sep="|", index=False)
        # password_manager_file = pandas.DataFrame(file_values)
        # password_manager_file.to_csv("password_manager_file.csv", mode='a', index=False, header=False, sep="|")

        # JSON WAY

        file_values = {
            website: {
                "email": email_username,
                "password": password,
            }
        }
        try:
            with open("data.json", "r") as data_file:
                # Reading old Data
                data = json.load(data_file)
                # Updating old Data with new data
                data.update(file_values)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving Updated data
                json.dump(file_values, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # Saving Updated data
                json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(height=500, width=500)
window.config(padx=50, pady=50, bg=LIGHT_BLUE)


canvas = Canvas(width=200, height=200, bg=LIGHT_BLUE, highlightthickness=0)
tomato_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=LIGHT_BLUE, fg=WHITE,  font=(FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=2)

email_username_label = Label(text="Email/Username:", bg=LIGHT_BLUE, fg=WHITE,  font=(FONT_NAME, 10, "bold"))
email_username_label.grid(column=0, row=3)

password_label = Label(text="Password:", bg=LIGHT_BLUE, fg=WHITE,  font=(FONT_NAME, 10, "bold"))
password_label.grid(column=0, row=4)

website_entry = Entry(bg=RED, fg=WHITE, width=26)
website_entry.grid(column=1, columnspan=1, row=2)

email_username_entry = Entry(bg=RED, fg=WHITE, width=45)
email_username_entry.grid(column=1, columnspan=2, row=3)
email_username_entry.insert(0, "example@gmail.com")

password_entry = Entry(bg=RED, fg=WHITE, width=26,)
password_entry.grid(column=1, row=4)

generate_button = Button(text="Generate Pass", bg=LIGHT_BLUE, fg=WHITE,  font=(FONT_NAME, 8), width=17, command=generate_password)
generate_button.grid(column=2, row=4)

search_button = Button(text="Search", bg=LIGHT_BLUE, fg=WHITE,  font=(FONT_NAME, 8), width=17, command=search)
search_button.grid(column=2, row=2)


add_button = Button(text="ADD", bg=LIGHT_BLUE, fg=WHITE, font=(FONT_NAME, 10, "bold"), width=33,
                    command=add_connection_information)
add_button.grid(column=1, columnspan=2, row=7)

window.mainloop()
