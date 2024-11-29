from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk, ImageSequence  # pip install Pillow
import time
import pygame  # pip install pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x500")


def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("G-ONE.gif")  # Enter the gif address
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    mixer.music.load("your_music_address.mp3")  # Enter the music file address
    mixer.music.play()

    for img in ImageSequence.Iterator(img):
        img = img.resize((1000, 500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()


play_gif()
root.mainloop()