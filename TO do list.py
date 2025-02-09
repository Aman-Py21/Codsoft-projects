import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark the selected task as done
def mark_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, task + " (Done)")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Function to clear all tasks
def clear_all_tasks():
    task_listbox.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(True, True)

# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Entry field for adding a task
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", font=("Arial", 14), bg="#4caf50", fg="white", command=add_task)
add_button.pack(pady=5)

# Frame for Listbox and Scrollbar
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

# Listbox to display tasks
task_listbox = tk.Listbox(listbox_frame, font=("Arial", 14), width=40, height=10, selectmode=tk.SINGLE)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for the Listbox
scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link scrollbar to listbox
task_listbox.config(yscrollcommand=scrollbar.set)

# Buttons to manage tasks
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Task", font=("Arial", 12), bg="#f44336", fg="white", width=12, command=delete_task)
delete_button.grid(row=0, column=0, padx=5)

mark_done_button = tk.Button(button_frame, text="Mark as Done", font=("Arial", 12), bg="#2196f3", fg="white", width=12, command=mark_done)
mark_done_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", font=("Arial", 12), bg="#ffc107", fg="black", width=12, command=clear_all_tasks)
clear_button.grid(row=1, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
