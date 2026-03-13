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

#sets up main window and geometry
root = tk.Tk()
root.title("File Explorer")
root.geometry("800x600")

#tracks current directory
current_path = os.getcwd()

#widget to display files
file_list = tk.Listbox(root)
file_list.pack(fill="both", expand=True)

#GUI main event loop
root.mainloop()