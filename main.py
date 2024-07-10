from tkinter import *
import pandas as pd
import random
import os
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#0C0C0C"
WHITE = "f4e9d4"
current_card = {}
to_learn = {}

# ---------------------------- BE SETUP ------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/en_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    eng_word = current_card["English"]
    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(card_title, text="English", fill=BLACK)
    canvas.itemconfig(card_word, text=eng_word, fill=BLACK)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_image, image=back_img)
    canvas.itemconfig(card_title, text="Russian", fill="WHITE")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="WHITE")

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_back():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    eng_word = current_card["English"]
    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(card_title, text="English", fill=BLACK)
    canvas.itemconfig(card_word, text=eng_word, fill=BLACK)
    flip_timer = window.after(3000, flip_card)

def restart():
    answer = messagebox.askyesno("Restart", "Are you sure you want to restart? All progress will be lost.")
    if answer:
        try:
            os.remove("data/words_to_learn.csv")
        except FileNotFoundError:
            pass
        finally:
            window.destroy()
            os.system("python " + __file__)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)

# Create the image
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create the buttons
yes_img = PhotoImage(file="images/right.png")
no_img = PhotoImage(file="images/wrong.png")
flip_img = PhotoImage(file="images/flip.png")
restart_img = PhotoImage(file="images/restart.png")

yes_button = Button(image=yes_img, highlightthickness=0, borderwidth=0, command=is_known)
yes_button.grid(column=1, row=1)

no_button = Button(image=no_img, highlightthickness=0, borderwidth=0, command=next_card)
no_button.grid(column=0, row=1)

flip_button = Button(image=flip_img, command=flip_back, highlightthickness=0, borderwidth=0)
flip_button.grid(column=0, row=2, columnspan=2)

restart_button = Button(image=restart_img, command=restart, highlightthickness=0, borderwidth=0)
restart_button.grid(column=0, row=2)

next_card()




window.mainloop()

