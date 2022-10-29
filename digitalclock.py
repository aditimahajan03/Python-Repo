# importing the entire module
from tkinter import * 
from tkinter.ttk import *
# import strftime funtion to retrieve system time

from time import strftime# we create a tkinter window
root = Tk()
root.title('CLOCK')
# this function will be used to display time  on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

# styling the label widget so the clock appears attractive
lbl = Label(root, font = ('Broadway', 30, 'bold'),
            background = 'white',
            foreground = 'black')
# centering the clock of the tkinter window
lbl.pack(anchor = 'center')
time()
mainloop()