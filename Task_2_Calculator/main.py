import tkinter as tk
import math

def on_button_click(value):
    current_text = entry.get()
    new_text = current_text + value
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def clear():
    entry.delete(0, tk.END)

def delete():
    current_text = entry.get()
    new_text = current_text[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate_power():
    try:
        result = str(eval(entry.get())) + '**'
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

size = 10
dim_x = 380
dim_y = 400
num = 0

colors = ['#000000','#40E0D0','#082567','#E6E6FA','#DAA520','#FF6F61','#50C878','#9966CC','#008080','#FD5E53','#6A0DAD']
index = len(colors)


def increase_size():
    global size, dim_x, dim_y, num

    num += 1
    theme = colors[index-num]
    theme1 = colors[num-index]
    root.configure(bg=f"{theme}")  # Change the theme
    entry.configure(bg=f"{theme1}")  # Change the theme
    if num >= 18:
        num = 0
    

    size += 20
    dim_x += 20
    if dim_y <= 450:
        dim_y += 50
    dimension = f"{dim_x}x{dim_y}"
    root.geometry(dimension)  # Increase the size of the window
    entry.grid(row=0, column=0, columnspan=10, pady=10, padx=10, ipadx=size)

def decrease_size():
    global size, dim_x, dim_y, num

    num += 1
    theme = colors[index-num]
    theme1 = colors[num-index]
    root.configure(bg=f"{theme}")  # Change the theme
    entry.configure(bg=f"{theme1}")  # Change the theme
    if num >= 18:
        num = 0

    if size > 20 and dim_x > 380:
        size -= 20
    if dim_x > 380:
        dim_x -= 20
    if dim_y > 400:
        dim_y -= 50

    dimension = f"{dim_x}x{dim_y}"
        # print(dimension)

    root.geometry(dimension)  # Increase the size of the window
    entry.grid(row=0, column=0, columnspan=10, pady=10, padx=10, ipadx=size)

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.configure(bg="#000000")  # Set background color to black

# Create an entry widget to display the calculations
entry = tk.Entry(root, font=("Helvetica", 20), justify="right", bg="#34495e", fg="white")  # Set entry colors for dark mode
entry.grid(row=0, column=0, columnspan=10, pady=10, padx=10, ipadx=10)

# Define button labels and positions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("DEL", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("^", 3, 4),
    ("0", 4, 0), ("00", 4, 1), (".", 4, 2), ("+", 4, 3), ("=", 4, 4),
    ("S", 5, 0),  # Button to decrease screen size
    ("L", 5, 4)  # Button to increase screen size
]

# Create buttons and arrange them in a grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Helvetica", 20), command=calculate, bg="#2ecc71", fg="white")  # Set button colors for dark mode
    elif text == "^":
        button = tk.Button(root, text=text, font=("Helvetica", 20), command=calculate_power, bg="#3498db", fg="white")
    elif text == "C":
        button = tk.Button(root, text=text, font=("Helvetica", 20), command=clear, bg="#e74c3c", fg="white")
    elif text == "DEL":
        button = tk.Button(root, text=text, font=("Helvetica", 20), command=delete, bg="#f39c12", fg="white")
    elif text == "S":
        button = tk.Button(root, text=text, font=("Helvetica", 20), command=decrease_size, bg="#91905f", fg="white")
    elif text == "L":
        button = tk.Button(root, text=text, font=("Helvetica", 20), command=increase_size, bg="#04405f", fg="white")
    else:
        button = tk.Button(root, text=text, font=("Helvetica", 20), command=lambda t=text: on_button_click(t), bg="#000000", fg="white")
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

# Set row and column weights to make buttons expandable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(6):
    root.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
root.mainloop()
