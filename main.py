from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#0C0C0C"
WHITE = "f4e9d4"
current_card = {}

# ---------------------------- BE SETUP ------------------------------- #
df= pd.read_csv("data/en_words.csv")
data = df.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(data)
    eng_word = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill=BLACK)
    canvas.itemconfig(card_word, text=eng_word, fill=BLACK)

def flip_card():
    global current_card
    canvas.itemconfig(card_image, image=back_img)
    canvas.itemconfig(card_title, text="Russian", fill="WHITE")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="WHITE")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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

yes_button = Button(image=yes_img, highlightthickness=0, borderwidth=0, command=next_card)
yes_button.grid(column=1, row=1)

no_button = Button(image=no_img, highlightthickness=0, borderwidth=0, command=next_card)
no_button.grid(column=0, row=1)

next_card()
window.after(3000, flip_card)


window.mainloop()

