import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = drop_var.get()
#    result_label.config(text=f"Selected item: {selected_item}")

# Create the main application window
root = tk.Tk()
root.title("Drop-down Menu")

# List of options for the drop-down menu
options = ["All", "Multiples", "Single"]

# Combobox variable to store the selected item
drop_var = tk.StringVar()

# Create the Combobox with the variable and options
dropdown_menu = ttk.Combobox(root, textvariable=drop_var, values=options)
dropdown_menu.pack(pady=10)

# Bind the event to handle selection change
dropdown_menu.bind("<<ComboboxSelected>>", on_select)

# Label to show the selected item
# result_label = tk.Label(root, text="")
# result_label.pack(pady=5)

root.mainloop()
