from tkinter import *
from time import *
def update():
    time_string=strftime("%H:%M:%S %p")
    time_label.config(text=time_string)

    day_string=strftime("%A")
    day_label.config(text=day_string)

    date_string=strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)


window=Tk()
window.title("Clock")

time_label=Label(window,font=("Arial",50),fg="green",bg="Black")
time_label.pack()

day_label=Label(window,font=("Ink Free",50),fg="Blue",bg="Black")
day_label.pack()

date_label=Label(window,font=("Arial",40),fg="red",bg="Black")
date_label.pack()
window.mainloop()


