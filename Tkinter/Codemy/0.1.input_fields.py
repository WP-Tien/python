from tkinter import *

root = Tk()

e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    myLabel = Label(root, text="My text is: " + e.get())
    myLabel.pack()

myButton = Button(root, text="Look! I clicked a Button!!", command=myClick)
myButton.pack()

root.mainloop()