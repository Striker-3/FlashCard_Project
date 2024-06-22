from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


canvas = Canvas(width=800 , height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_image)
canvas.create_text(400,150,text="Title" , font=("Arial" , 40 , "italic"))
canvas.create_text(400,270,text="Word" , font=("Arial" , 50 , "bold"))
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_button_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_button_image,bg=BACKGROUND_COLOR , highlightthickness=0)
cross_button.grid(row=1,column=0)

check_button_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_image,bg=BACKGROUND_COLOR , highlightthickness=0)
check_button.grid(row=1,column=1)




window.mainloop()