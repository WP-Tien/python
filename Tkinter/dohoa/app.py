import tkinter as tk
from tkmacosx import Button

# Tkinter version
# print(tk.TkVersion)

# Tạo cửa sổ ứng dụng
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

# Ngăn không cho cửa sổ thay đổi kích thước
root.resizable(False, False)

# Theme color
root.config(bg="#f0f0f0") # Nền màu xám nhạt

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        print("Please enter a task")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        print("Vui lòng chọn một tác vụ để xoá!")

def clear_all_tasks():
    task_listbox.delete(0, tk.END)
    
def mark_complete():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        
        # Kiểm tra xem tác vụ đã được đánh dấu hoàn thành chưa
        if not task.startswith("✓ "):
            # Đánh dấu là hoàn thành với dấu kiểm
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, "✓ " + task)
            task_listbox.itemconfig(selected_index, fg="gray")
    except IndexError:
        print("Vui lòng chọn một tác vụ để đánh dấu là hoàn thành!")
        
# Header style
header_frame = tk.Frame(root, bg="#4a7c9e")
header_frame.pack(fill=tk.X) # fill=tk.X, chúng ta làm cho frame trải dài theo chiều ngang qua cửa sổ. 

header_label = tk.Label(header_frame, text="📝 My To-Do List", font=("Arial", 18, "bold"), bg="#4a7c9e", fg="white")
header_label.pack(pady=15)


# style cho input
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=20)

task_entry = tk.Entry(input_frame, width=35, font=("Arial", 13),
                      bd=2, relief=tk.GROOVE)
task_entry.pack(side=tk.LEFT, padx=10, ipady=5)
task_entry.bind('<Return>', lambda event: add_task())

add_button = tk.Button(input_frame, text="Add Task", width=12, 
                      font=("Arial", 11, "bold"),
                        cursor="hand2",
                      command=add_task)
add_button.pack(side=tk.LEFT)

# task_entry = tk.Entry(root, width=35, font=("Arial", 12))
# task_entry.pack(pady=10)
# add_button = tk.Button(root, text="Add Task", width=20, font=("Arial", 10), command=add_task)
# add_button.pack(pady=5)

list_frame = tk.Frame(root, bg="#f0f0f0")
list_frame.pack(pady=10, padx=20)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)

task_listbox = tk.Listbox(list_frame, width=55, height=14, 
                         font=("Arial", 11),
                         bd=2, relief=tk.SUNKEN,
                         selectmode=tk.SINGLE,
                         activestyle='none',
                         yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 10))
# task_listbox.pack(pady=10)

# tạo frame đặt các nút
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# mark_button = tk.Button(button_frame, text="✓ Mark Complete", width=15, 
#                         font=("Arial", 10, "bold"),
#                         bd=0, cursor="hand2",
#                         command=mark_complete)

mark_button = Button(button_frame, text="✓ Mark Complete", 
                        font=("Arial", 10, "bold"),
                        bd=0, cursor="hand2",
                        bg="#4CAF50",       # background
                        fg="white",         # text color
                        activebackground="#45a049",
                        activeforeground="white",
                        command=mark_complete)
mark_button.grid(row=0, column=0, padx=8)

delete_button = tk.Button(button_frame, text="✕ Delete Task", width=15, 
                         font=("Arial", 10, "bold"),
                         bd=0, cursor="hand2",
                         command=delete_task)
delete_button.grid(row=0, column=1, padx=8)

clear_button = tk.Button(button_frame, text="Clear All", width=15, 
                        font=("Arial", 10, "bold"),
                        bd=0, cursor="hand2",
                        command=clear_all_tasks)
clear_button.grid(row=0, column=2, padx=8)
# button_frame = tk.Frame(root)
# button_frame.pack(pady=10)

# mark_button = tk.Button(button_frame, text="Mark Complete", width=15, font=("Arial", 10), command=mark_complete)
# mark_button.grid(row=0, column=0, padx=5)

# delete_button = tk.Button(button_frame, text="Delete Task", width=15, font=("Arial", 10), command=delete_task)
# delete_button.grid(row=0, column=1, padx=5)

# clear_button = tk.Button(button_frame, text="Clear All", width=15, font=("Arial", 10), command=clear_all_tasks)
# clear_button.grid(row=0, column=2, padx=5)

# Footer
footer_label = tk.Label(root, text="Chọn một tác vụ và sử dụng các nút để quản lý nó", 
                        font=("Arial", 9, "italic"),
                        bg="#f0f0f0", fg="#666666")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Bắt đầu vòng lặp sự kiện
root.mainloop()

'''
Chúng ta nhập Tkinter và đặt biệt danh là tk cho tiện lợi.
root = tk.Tk() tạo cửa sổ ứng dụng chính.
Chúng ta đặt tiêu đề cửa sổ bằng cách sử dụng root.title().
root.geometry("400x500") đặt kích thước cửa sổ.
root.resizable(False, False) ngăn người dùng thay đổi kích thước cửa sổ. Tham số đầu tiên kiểm soát thay đổi kích thước chiều ngang, tham số thứ hai kiểm soát chiều dọc.
Cuối cùng, root.mainloop() bắt đầu vòng lặp sự kiện. Điều này rất quan trọng! Nếu không có nó, cửa sổ của bạn sẽ xuất hiện và ngay lập tức đóng lại.
'''