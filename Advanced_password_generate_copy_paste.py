import tkinter as tk
import random
import string
import pyperclip  # for copy (write terminal : pip install pyperclip)


# Password strength check
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

# Password generate function
def generate():
    try:
        length = int(entry_len.get())
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(length))
        history_listbox.insert(0, password)
        # show password
        result_label.config(text=password)

        # strength meter
        strength_text, color = check_strength(password)
        strength_label.config(text=f"Strength: {strength_text}", fg=color)
    except ValueError:
        result_label.config(text="Enter valid number!")


# copy function
def copy_to_clipboard():
    password = result_label.cget("text")
    if password and password != "Enter valid number!":
        pyperclip.copy(password)


# Main window setup
root = tk.Tk()
root.title("Advanced Password Gen")
root.geometry("400x400")

# GUI design
tk.Label(root, text="Password length:", font=("Arial", 14, "bold")).pack(pady=20)
entry_len = tk.Entry(root)
entry_len.pack()

generate_button = tk.Button(root, text="Generate Your Password", font=("Arial", 14, "bold"),
                            command=generate, bg="White",fg="Blue")
generate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="Black")
result_label.pack(pady=20)

# history label
tk.Label(root, text="Password History:", font=("Arial", 10)).pack(pady=5)

# listbox and scrollbar
history_frame = tk.Frame(root)
history_frame.pack(pady=5)

scrollbar = tk.Scrollbar(history_frame, orient=tk.VERTICAL)
history_listbox = tk.Listbox(history_frame, width=40, height=5, yscrollcommand=scrollbar.set)

scrollbar.config(command=history_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
history_listbox.pack(side=tk.LEFT)

strength_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
strength_label.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard, bg="white").pack(pady=20)

root.mainloop()
