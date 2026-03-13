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

#GUI main event loop
root.mainloop()