from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('/Applications/XAMPP/xamppfiles/htdocs/python/Tkinter/Codemy/ico.png')

# Define target dimensions (width, height)
target_width = 250
target_height = 200

# 2. Open the image using Pillow's Image.open()
# Replace "sample.jpg" with your image file path
pil_image = Image.open('/Applications/XAMPP/xamppfiles/htdocs/python/Tkinter/Codemy/ico.png')

# 3. Resize the image
# The resize method takes a tuple (width, height)
# Image.LANCZOS is a high-quality resampling filter (ANTIALIAS is deprecated)
resized_image = pil_image.resize((target_width, target_height), Image.LANCZOS)

# 4. Convert the resized image to a Tkinter-compatible PhotoImage object
my_img = ImageTk.PhotoImage(resized_image)

# 5. Display the image in a Tkinter widget (e.g., a Label or Canvas)
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()