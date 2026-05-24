from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def open():
    global my_img1
    top = Toplevel()
    top.title('My Second Window')
    target_width = 250
    target_height = 200
    pil_image1 = Image.open("/Applications/XAMPP/xamppfiles/htdocs/python/Tkinter/Codemy/images/img1.jpg")
    resized_image1 = pil_image1.resize((target_width, target_height), Image.LANCZOS)
    my_img1 = ImageTk.PhotoImage(resized_image1)
    Label(top, image=my_img1).pack()
    Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()