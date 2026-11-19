from tkinter import *
from tkinter import colorchooser
def click_me():
    color=colorchooser.askcolor()
    print(color)

window=Tk()
window.title("My first Gui project")
window.geometry("500x500")
button=Button(window,text="Click me",bg="blue",fg="white",command=click_me)
button.pack()

window.mainloop()