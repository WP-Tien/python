# side = top or bottom 
# widget can be as wide as the container
# expand determines (xác định) the height

# side = left or right
# widget can be as heigh as the container
# expand determines the width

# by default, widgets will only occupy (chiếm) the space they need to display the content
# But they can occupy more space!
# if side is top or bottom, widgets can occupy the entire width of the container

# expand tells the widgets that is can take up all the available space in one direction

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack')
window.geometry('400x600')

# widgets
label1 = tk.Label(window, text = 'First label', bg = 'red')
label2 = tk.Label(window, text = 'Label 2', background = 'blue')
label3 = tk.Label(window, text = 'Last of the labels', background = 'green')
button = tk.Button(window, text = 'Button')

# layout
# label1.pack(side = 'top', expand = True)
# label2.pack(side = 'top')
# label3.pack(side = 'top', expand = True)
# button.pack(side = 'top')

# label1.pack(side = 'left', expand = True)
# label2.pack(side = 'left')
# label3.pack(side = 'left', expand = True)
# button.pack(side = 'left')

label1.pack(side = 'top', fill = 'both', ipady = 50, padx = 100)
label2.pack(side = 'top', expand = True)
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top', expand = True, fill = 'y')

# run
window.mainloop()