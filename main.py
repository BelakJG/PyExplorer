import tkinter as tk
from logging import exception
from tkinter import ttk
import os
import subprocess

def populate_tree(parent, path):
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                node = file_tree.insert(parent, "end", text=item, values=[full_path])

                file_tree.insert(node, "end")

    except PermissionError:
        pass

def open_node(event):
    node = file_tree.focus()
    values = file_tree.item(node)["values"]
    if not values:
        return

    path = values[0]
    children = file_tree.get_children(node)
    if children:
        first_child = children[0]
        if not file_tree.item(first_child)["values"]:
            file_tree.delete(first_child)
            populate_tree(node, path)

def show_files(event):
    node = file_tree.focus()
    values = file_tree.item(node)["values"]
    if not values:
        return

    path = values[0]

    file_list.delete(*file_list.get_children())

    try:
        path_var.set(path)
        for item in os.listdir(path):
            full_path = os.path.join(path, item)

            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                ext = os.path.splitext(item)[1]

                file_list.insert("", "end", values=(item, size, ext))
    except PermissionError:
        pass

def open_file(event):
    item = file_list.focus()

    values = file_list.item(item)["values"]
    if not values:
        return

    filename = values[0]
    path = os.path.join(path_var.get(), filename)

    try:
        subprocess.Popen(["xdg-open", path])
    except Exception as e:
        print("Could not open file: ", e)


#sets up main window and geometry
root = tk.Tk()
root.title("File Explorer")
root.geometry("800x600")

#Pane to allow resizeable panels
paned = tk.PanedWindow(root, orient="horizontal")
paned.pack(fill="both", expand=True)

file_tree = ttk.Treeview(paned)
paned.add(file_tree, width=300)

#sets root to root director on linux or windows
root_node = file_tree.insert("", "end", text=os.path.abspath(os.sep), values=[os.path.abspath(os.sep)], open=True)
populate_tree(root_node, os.path.abspath(os.sep))

file_tree.bind("<<TreeviewOpen>>", open_node)

file_list =ttk.Treeview(paned, columns=("name", "size"), show="headings")
file_list.heading("name", text="Name")
file_list.heading("size", text="Size")
paned.add(file_list)

file_list.bind("<Double-Button-1>", open_file)

file_tree.bind("<<TreeviewSelect>>", show_files)

path_var = tk.StringVar()
path_bar = tk.Entry(root, textvariable=path_var)
path_bar.pack(fill="x")

#GUI main event loop
root.mainloop()