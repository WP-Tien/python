from tkinter import *
from tkinter import messagebox

root = Tk()

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World!")
    if response == 1:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()
    
Button(root, text="Popup", command=popup).pack()

mainloop()