import tkinter as tk
from tkinter import messagebox

# Function to display a message when the button is clicked
def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Greeting", f"Hello, {user_input}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

# Create a button
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=20)

# Run the main event loop
root.mainloop()
