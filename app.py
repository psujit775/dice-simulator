from tkinter import *
import random
from playsound import playsound

window = Tk()
window.title('Dice Simulator')
window.geometry("440x400")


def new_img():
    # Pick a new number
    number = random.randint(1, 6)
    # Add '.png' to number
    myimg = 'resources/'+str(number) + '.png'
    # Return the image name
    return myimg


def roll():
    global img
    myimg = new_img()
    playsound('resources/dice.mp3')
    canvas = Canvas(window)
    canvas.place(x=120, y=100)
    img = PhotoImage(file=myimg)
    canvas.create_image(100, 100, image=img)


btn = Button(window, text="Click to Roll", fg='blue', command=roll)
btn.place(x=170, y=0)


window.mainloop()
