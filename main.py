# from tkinter import *
# import pandas
# import random
#
# BACKGROUND_COLOR = "#B1DDC6"
#
# current_card ={}
# letter_from_data = {}
#
# try:
#     data = pandas.read_csv("data/unknown_words.csv")
#
# except FileNotFoundError:
#     original_data = pandas.read_csv("data/french_words.csv")
#     letter_from_data = original_data.to_dict(orient="records")
#
# else:
#     letter_from_data = data.to_dict(orient="records")
#
#
#
# def next_card():
#     global current_card , flip_timer
#     window.after_cancel(flip_timer)
#     current_card =  random.choice(letter_from_data)
#     canvas.itemconfig(card_title , text = "French" , fill="black")
#     canvas.itemconfig(card_word , text = current_card["French"] , fill="black")
#     canvas.itemconfig(card_background , image = card_front_image)
#     flip_timer = window.after(3000 , func=flip_card)
#
# def flip_card():
#     canvas.itemconfig(card_title , text = "English" , fill = "white")
#     canvas.itemconfig(card_word , text = current_card["English"] , fill = "white")
#     canvas.itemconfig(card_background , image = card_back_image )
#
#
# def known_card():
#     letter_from_data.remove(current_card)
#     new_data = pandas.DataFrame(letter_from_data)
#     new_data.to_csv("data/unknown_words.csv" , index=False)
#     next_card()
#
# window = Tk()
# window.title("Flashy")
# window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
#
# flip_timer = window.after(3000,func=flip_card)
#
# canvas = Canvas(width=800 , height=526)
# card_front_image = PhotoImage(file="images/card_front.png")
# card_back_image = PhotoImage(file="images/card_back.png")
# card_background =  canvas.create_image(400,263,image=card_front_image)
# card_title = canvas.create_text(400,150,text="" , font=("Arial" , 40 , "italic"))
# card_word =  canvas.create_text(400,270,text="" , font=("Arial" , 50 , "bold"))
# canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
# canvas.grid(row=0,column=0,columnspan=2)
#
# cross_button_image = PhotoImage(file="images/wrong.png")
# cross_button = Button(image=cross_button_image,bg=BACKGROUND_COLOR , highlightthickness=0 , command=next_card)
# cross_button.grid(row=1,column=0)
#
# check_button_image = PhotoImage(file="images/right.png")
# check_button = Button(image=check_button_image,bg=BACKGROUND_COLOR , highlightthickness=0 , command=known_card)
# check_button.grid(row=1,column=1)
#
# next_card()
#
#
# window.mainloop()


# from tkinter import *
# import pandas
# import random
# from gtts import gTTS
# import pygame
# import os
# import time
#
# BACKGROUND_COLOR = "#B1DDC6"
#
# current_card = {}
# letter_from_data = {}
#
# try:
#     data = pandas.read_csv("data/unknown_words.csv")
# except FileNotFoundError:
#     original_data = pandas.read_csv("data/french_words.csv")
#     letter_from_data = original_data.to_dict(orient="records")
# else:
#     letter_from_data = data.to_dict(orient="records")
#
#
# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(letter_from_data)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#     canvas.itemconfig(card_background, image=card_front_image)
#     flip_timer = window.after(3000, func=flip_card)
#
#
# def flip_card():
#     canvas.itemconfig(card_title, text="English", fill="white")
#     canvas.itemconfig(card_word, text=current_card["English"], fill="white")
#     canvas.itemconfig(card_background, image=card_back_image)
#
#
# def known_card():
#     letter_from_data.remove(current_card)
#     new_data = pandas.DataFrame(letter_from_data)
#     new_data.to_csv("data/unknown_words.csv", index=False)
#     next_card()
#
#
# def pronounce_word():
#     if current_card:
#         word = current_card["French"]
#         tts = gTTS(text=word, lang='fr')
#
#         # Generate a unique filename using the current time
#         unique_filename = f"word_{int(time.time())}.mp3"
#
#         # Save the TTS output to the unique filename
#         tts.save(unique_filename)
#
#         # Play the audio file
#         pygame.mixer.music.load(unique_filename)
#         pygame.mixer.music.play()
#
#         # Schedule the file to be deleted after playback
#         window.after(4000, lambda: os.remove(unique_filename))
#
#
# # Initialize Pygame mixer
# pygame.mixer.init()
#
# window = Tk()
# window.title("Flashy")
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#
# flip_timer = window.after(3000, func=flip_card)
#
# canvas = Canvas(width=800, height=526)
# card_front_image = PhotoImage(file="images/card_front.png")
# card_back_image = PhotoImage(file="images/card_back.png")
# card_background = canvas.create_image(400, 263, image=card_front_image)
# card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
# card_word = canvas.create_text(400, 270, text="", font=("Arial", 50, "bold"))
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=3)
#
# cross_button_image = PhotoImage(file="images/wrong.png")
# cross_button = Button(image=cross_button_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
# cross_button.grid(row=1, column=0)
#
# check_button_image = PhotoImage(file="images/right.png")
# check_button = Button(image=check_button_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_card)
# check_button.grid(row=1, column=2)
#
# pronounce_button_image = PhotoImage(file="images/pngwing.com.png")  # Make sure to have a speaker icon image
# pronounce_button = Button(image=pronounce_button_image, bg=BACKGROUND_COLOR, highlightthickness=0,
#                           command=pronounce_word)
# pronounce_button.grid(row=1, column=1)
#
# next_card()
#
# window.mainloop()
#
# # Ensure the audio file is cleaned up
# if os.path.exists("word.mp3"):
#     pygame.mixer.quit()
#     os.remove("word.mp3")



from tkinter import *
import pandas
import random
from gtts import gTTS
import pygame
import os
import time

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
letter_from_data = {}
audio_files = []

try:
    data = pandas.read_csv("data/unknown_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    letter_from_data = original_data.to_dict(orient="records")
else:
    letter_from_data = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(letter_from_data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def known_card():
    letter_from_data.remove(current_card)
    new_data = pandas.DataFrame(letter_from_data)
    new_data.to_csv("data/unknown_words.csv", index=False)
    next_card()


def pronounce_word():
    if current_card:
        word = current_card["French"]
        tts = gTTS(text=word, lang='fr')

        # Generate a unique filename using the current time
        unique_filename = f"word_{int(time.time())}.mp3"
        audio_files.append(unique_filename)

        # Save the TTS output to the unique filename
        tts.save(unique_filename)

        # Play the audio file
        pygame.mixer.music.load(unique_filename)
        pygame.mixer.music.play()

        # Schedule the file to be deleted after playback
        window.after(4000, lambda: delete_audio_file(unique_filename))


def delete_audio_file(filename):
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except PermissionError:
            # Retry deleting the file after some time
            window.after(1000, lambda: delete_audio_file(filename))


# Initialize Pygame mixer
pygame.mixer.init()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 270, text="", font=("Arial", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

cross_button_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_button_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_button_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_card)
check_button.grid(row=1, column=2)

pronounce_button_image = PhotoImage(file="images/pngwing.com.png")  # Make sure to have a speaker icon image
pronounce_button = Button(image=pronounce_button_image, bg=BACKGROUND_COLOR, highlightthickness=0,
                          command=pronounce_word)
pronounce_button.grid(row=1, column=1)

next_card()

window.mainloop()

# Ensure all audio files are cleaned up
pygame.mixer.quit()
for filename in audio_files:
    if os.path.exists(filename):
        os.remove(filename)
