import tkinter
import random


def RandomNumber():
    MyRandom = random.randint(1, 6)
    dice_thrown.configure(text="Dice thown" + str(MyRandom))


window = tkinter.Tk()

MyTitle = tkinter.Label(window, text="Test APP", font="Helvetica 16 bold")
MyTitle.pack()

MyButton = tkinter.Button(window, text="Test Button", command=RandomNumber)
MyButton.pack()

dice_thrown = tkinter.Label(window, font="Helvetica 16 bold")
dice_thrown.pack()

window.mainloop()
