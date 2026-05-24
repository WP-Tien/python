from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Codemy.com Image Viwer')
root.iconbitmap('/Applications/XAMPP/xamppfiles/htdocs/python/Tkinter/Codemy/ico.png')

target_width = 250
target_height = 200

pil_image1 = Image.open("/Applications/XAMPP/xamppfiles/htdocs/python/Tkinter/Codemy/images/img1.jpg")
resized_image1 = pil_image1.resize((target_width, target_height), Image.LANCZOS)
my_img1 = ImageTk.PhotoImage(resized_image1)

pil_image2 = Image.open("/Applications/XAMPP/xamppfiles/htdocs/python/Tkinter/Codemy/images/img2.jpg")
resized_image2 = pil_image2.resize((target_width, target_height), Image.LANCZOS)
my_img2 = ImageTk.PhotoImage(resized_image2)

pil_image3 = Image.open("/Applications/XAMPP/xamppfiles/htdocs/python/Tkinter/Codemy/images/img3.jpg")
resized_image3 = pil_image3.resize((target_width, target_height), Image.LANCZOS)
my_img3 = ImageTk.PhotoImage(resized_image3)

image_list = [my_img1, my_img2, my_img3]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number ==3:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    # Update status
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update status
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()