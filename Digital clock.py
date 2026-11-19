
from tkinter import *
from tkinter import font
from time import strftime

# Create the window
root = Tk()

# Window settings
root.title("Digital Clock")
root.geometry("600x200")
root.configure(bg="black")

# Load digital font
my_font = font.Font(family="DS-DIGIT", size=100)

# Create the clock label
time_label = Label(root,
                   font=my_font,
                   background="black",
                   foreground="green")

time_label.pack(anchor="center", expand=True)


# Function to update time
def update_time():
    current_time = strftime("%I:%M:%S %p")
    time_label.config(text=current_time)

    time_label.after(1000, update_time)


# Start the clock
update_time()

# Run the application
root.mainloop()
