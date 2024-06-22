from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
letter_from_data = data.to_dict(orient="records")

def next_card():
    current_card =  random.choice(letter_from_data)
    canvas.itemconfig(card_title , text = "French")
    canvas.itemconfig(card_word , text = current_card["French"])


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


canvas = Canvas(width=800 , height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_image)
card_title = canvas.create_text(400,150,text="" , font=("Arial" , 40 , "italic"))
card_word =  canvas.create_text(400,270,text="" , font=("Arial" , 50 , "bold"))
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_button_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_button_image,bg=BACKGROUND_COLOR , highlightthickness=0 , command=next_card)
cross_button.grid(row=1,column=0)

check_button_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_image,bg=BACKGROUND_COLOR , highlightthickness=0 , command=next_card)
check_button.grid(row=1,column=1)

next_card()


window.mainloop()