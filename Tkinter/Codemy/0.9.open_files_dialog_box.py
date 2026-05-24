from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Codemy.com Image Viewer")

my_image_label = None

def open():
    global my_image, my_image_label # Tkinter cần giữ reference ảnh để tránh bị garbage collection 👍
    
    file_path = filedialog.askopenfilename(
        initialdir="/", 
        title="Select A File", 
        filetypes=(("JPG files", "*.jpg"), ("All files", "*.*"))
    )
    
    if not file_path:
        return # Người dùng bấm Cancel
    
    my_image = ImageTk.PhotoImage(Image.open(file_path))

    if my_image_label:
        my_image_label.config(image=my_image)
    else:
        my_image_label = Label(root, image=my_image)
        my_image_label.pack()
    
my_btn = Button(root, text="Open File", command=open).pack(pady=10)

root.mainloop()