from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

if os.path.exists("words_to_learn.csv"):
    data = pandas.read_csv("words_to_learn.csv")
else:
    data = pandas.read_csv("/home/kirubagar/Downloads/flash-card-project-start/data/kannada_words.csv")

to_learn = data.to_dict(orient = "records")

current_card = {}


#canvas
canvas = Canvas(width= 900, height=700,bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid()

card_front_img = PhotoImage(file="/home/kirubagar/Downloads/flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="/home/kirubagar/Downloads/flash-card-project-start/images/card_back.png")


card_background = canvas.create_image(450, 300, image=card_front_img)
card_title = canvas.create_text(440, 180, text="",font=("Ariel",30, "italic"))
card_word = canvas.create_text(440, 300, text="", font=("Ariel",30, "bold"))

flip_timer = window.after(3000, func=lambda: None)



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Kannada", fill="black")
    canvas.itemconfig(card_word, text=current_card["Kannada"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()



#button
wrong_button_image = PhotoImage(file="/home/kirubagar/Downloads/flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0, command=next_card)

canvas.create_window(250, 620, window=wrong_button)

right_button_image = PhotoImage(file="/home/kirubagar/Downloads/flash-card-project-start/images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, borderwidth=0, command=is_known)

canvas.create_window(650, 620, window=right_button)

next_card()



window.mainloop()

