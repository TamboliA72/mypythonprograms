#/usr/bin/python - Program for adding the buttons in the GUI.....

#importing the libraries for creating GUI
from tkinter import *
from tkinter import messagebox

#creating a tkinter object 
window = Tk()

window.title("Welcome to Button app")
window.geometry('350x200')

#adding a lable in the window
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

#handing the click event for a button
def clicked():
    messagebox.showinfo('Button Clicked','Yes you clicked the button!!!!')

#creating a button named "click me"
btn = Button(window, text="Click Me",command = clicked,bg="blue",fg="red")
btn.grid(column=1, row=0)

#creating a button named "kick me"
btn = Button(window, text="Kick Me",command = clicked)
btn.grid(column=3, row=0)

window.mainloop()
