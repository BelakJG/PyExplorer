import tkinter as tk
import os

def load_files(path):
    file_list.delete(0, tk.END)
    files = os.listdir(path)
    for file in files:
        file_list.insert(tk.END, file)

def open_items(event):
    global current_path

    selection = file_list.get(file_list.curselection())
    path = os.path.join(current_path, selection)

    if os.path.isdir(path):
        current_path = path
        load_files(current_path)

def go_up():
    global current_path
    current_path = os.path.dirname(current_path)
    load_files(current_path)

#sets up main window and geometry
root = tk.Tk()
root.title("File Explorer")
root.geometry("800x600")

#tracks current directory
current_path = os.getcwd()

#widget to display files
file_list = tk.Listbox(root)
file_list.pack(fill="both", expand=True)
load_files(current_path)

file_list.bind("<Double-Button-1>", open_items)

up_button = tk.Button(root, text="Up", command=go_up)
up_button.pack()

#GUI main event loop
root.mainloop()