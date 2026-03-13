import tkinter as tk
from tkinter import ttk
import os

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
    path = file_tree.item(node)["values"][0]

    file_tree.delete(*file_tree.get_children(node))
    populate_tree(node, path)

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
root_node = file_tree.insert("", "end", text=os.path.abspath(os.sep), open=True)

file_tree.bind("<<TreeviewOpen>>", open_node)

file_list =ttk.Treeview(paned, columns=("size", "type"), show="headings")
file_list.heading("size", text="Size")
file_list.heading("type", text="type")
paned.add(file_list)

#GUI main event loop
root.mainloop()