from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    welcome_message.config(text="Timer")
    global REPS
    REPS = 0
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        welcome_message.config(text="Break", fg=RED)
        REPS = 0
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        welcome_message.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        welcome_message.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if REPS % 2 == 0:
            ticks_to_show = math.floor(REPS / 2)
            tick_label.config(text=f"✔" * ticks_to_show)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


welcome_message = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
welcome_message.pack()


canvas = Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

start_button = Button(text="Start", bg=RED, font=(FONT_NAME, 15, "bold"), fg=GREEN, command=start_timer)
start_button.place(x=-50, y=285)

reset_button = Button(text="Reset", bg=RED, font=(FONT_NAME, 15, "bold"), fg=GREEN, command=reset_timer)
reset_button.place(x=160, y=285)

tick_label = Label(bg=YELLOW, font=(FONT_NAME, 15, "bold"), fg=GREEN, pady=10)
tick_label.pack()



window.mainloop()
