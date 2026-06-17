import tkinter as tk
import random
import string
import pyperclip


# --- All Functions ---
def check_strength(password):
    if len(password) < 8:
        return "Weak (Too short)", "Red"
    elif any(char.isdigit() for char in password) and any(char in string.punctuation for char in password):
        return "Strong", "Green"
    else:
        return "Medium", "Orange"


def save_to_file(password):
    with open("password_history.txt", "a") as file:
        file.write(password + "\n")


def generate_password():
    try:
        length = int(entry_len.get())
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(length))

        history_listbox.insert(0, password)
        result_label.config(text=password)
        save_to_file(password)

        strength_text, color = check_strength(password)
        strength_label.config(text=f"Strength: {strength_text}", fg=color)
    except ValueError:
        result_label.config(text="Enter valid number!")


def copy_to_clipboard():
    password = result_label.cget("text")
    if password and password != "Enter valid number!":
        pyperclip.copy(password)


def clear_history():
    history_listbox.delete(0, tk.END,)


# --- Main Window Setup ---
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x500")

# --- GUI Design ---
tk.Label(root, text="Password Length:", font=("Arial", 14, "bold"),bg="White", fg="Black").pack(pady=10)
entry_len = tk.Entry(root)
entry_len.pack()

generate_button = tk.Button(root, text="Generate Your Password", font=("Arial", 14), command=generate_password, bg="White",
                            fg="Blue")
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="Black")
result_label.pack(pady=10)

strength_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
strength_label.pack()

# History label and Listbox
tk.Label(root, text="Password History:", font=("Arial", 10, "bold"),).pack(pady=5)
history_frame = tk.Frame(root)
history_frame.pack(pady=5)

scrollbar = tk.Scrollbar(history_frame, orient=tk.VERTICAL)
history_listbox = tk.Listbox(history_frame, width=40, height=5, yscrollcommand=scrollbar.set)
scrollbar.config(command=history_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
history_listbox.pack(side=tk.LEFT)

# Buttons
tk.Button(root, text="Copy to Clipboard", font=("Arial", 10,"bold"), command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Clear History", font=("Arial", 10,"bold"),fg="Red", command=clear_history).pack(pady=5)

root.mainloop()
