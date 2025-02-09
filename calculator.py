import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            input_var.set(expression)
    elif text == "C":
        expression = ""
        input_var.set(expression)
    else:
        expression += text
        input_var.set(expression)

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("450x450")
root.resizable(False, False)

# Variables
expression = ""
input_var = tk.StringVar()

# Input Field
input_frame = tk.Frame(root)
input_frame.pack(pady=10)
input_field = tk.Entry(input_frame, textvariable=input_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
input_field.grid(row=0, column=0, ipadx=8, ipady=8, columnspan=4)

# Button Layout
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack()

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(button_frame, text=btn_text, font=("Arial", 18), width=5, height=2, relief=tk.RAISED, bg="#f5f5f5")
        btn.grid(row=i, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)

# Run the main loop
root.mainloop()
