import tkinter as tk
from tkinter import ttk
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

#Pane to allow resizeable panels
paned = tk.PanedWindow(root, orient="horizontal")
paned.pack(fill="both", expand=True)

file_tree = ttk.Treeview(paned)
paned.add(file_tree, width=300)

#GUI main event loop
root.mainloop()