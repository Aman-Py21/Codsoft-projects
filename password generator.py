import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError("Length must be positive.")
        
        # Characters for password generation
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        
        # Display the password in the Text widget
        password_display.config(state="normal")  # Enable editing temporarily
        password_display.delete(1.0, tk.END)  # Clear the previous content
        password_display.insert(tk.END, password)  # Insert the new password
        password_display.config(state="disabled")  # Disable editing
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for the length.")

def copy_to_clipboard():
    password = password_display.get(1.0, tk.END).strip()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Keeps clipboard updated
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")
root.resizable(True, True)

# Variables
length_var = tk.StringVar()

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Length Input
length_label = tk.Label(root, text="Enter the desired length of the password:", font=("Arial", 12))
length_label.pack(pady=5)

length_entry = tk.Entry(root, textvariable=length_var, font=("Arial", 14), width=10, justify="center")
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), bg="#4caf50", fg="white", command=generate_password)
generate_button.pack(pady=20)

# Display Password
password_label = tk.Label(root, text="Generated Password:", font=("Arial", 12))
password_label.pack(pady=5)

password_display = tk.Text(root, font=("Arial", 12), wrap="word", height=4, width=50, state="disabled", bg="#f5f5f5", relief=tk.RIDGE)
password_display.pack(pady=10)

# Copy Button
copy_button = tk.Button(root, text="Copy Password", font=("Arial", 12), bg="#2196f3", fg="white", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
root.mainloop()
