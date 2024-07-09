from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)

# Create the image
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create the buttons
yes_img = PhotoImage(file="images/right.png")
no_img = PhotoImage(file="images/wrong.png")

yes_button = Button(image=yes_img, highlightthickness=0, borderwidth=0)
yes_button.grid(column=1, row=1)

no_button = Button(image=no_img, highlightthickness=0, borderwidth=0)
no_button.grid(column=0, row=1)



window.mainloop()

