from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import pyperclip
import json

# ------------------------------------Theme Colour--------------------------------------#
colors_list = ['#40E0D0','#082567','#E6E6FA','#DAA520','#FF6F61','#50C878','#9966CC','#008080','#FD5E53','#6A0DAD']
colour = choice(colors_list)
def theme():
    colour = choice(colors_list)

    window.config(bg=colour)
    canvas.config(bg=colour)
    website_label.config(bg=colour)
    website_entry.config(bg=colour)
    search_button.config(bg=colour)
    email_label.config(bg=colour)
    email_entry.config(bg=colour)
    pass_digit_label.config(bg=colour)
    pass_digit_entry.config(bg=colour)
    theme_button.config(bg=colour)
    pass_digit_label.config(bg=colour)
    pass_digit_entry.config(bg=colour)
    password_label.config(bg=colour)
    password_entry.config(bg=colour)
    generate_password_button.config(bg=colour)
    add_button.config(bg=colour)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def generate_password():

    digit = pass_digit_entry.get()
    if len(digit)==0 or digit==None:
            messagebox.showinfo(title="Oops", message="Password Digit can't be zero or none.")
    
    else:
        try:
            digit = int(digit)
            
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            password_letters = [choice(letters) for _ in range(digit)]
            password_symbols = [choice(symbols) for _ in range(digit)]
            password_numbers = [choice(numbers) for _ in range(digit)]

            password_list = password_letters + password_symbols + password_numbers
            shuffle(password_list)
            password_list = password_list[:digit]

            password = "".join(password_list)
            password_entry.insert(0, password)
            pyperclip.copy(password)
        except:
            messagebox.showinfo(title="Oops", message="Digit should be an integer value.")
    


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", 'r') as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving the data
                json.dump(new_data, data_file, indent=4)

        else:       # else block only work when try block execute
            # updating data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving the data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            pass_digit_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()

    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File doesn't exist!")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email}\nPassword : {password}")

        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exist in database")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=colour)

canvas = Canvas(height=200, width=200,bg=colour)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website : ", bg=colour)
website_label.grid(row=1, column=0, padx=2, pady=2)
email_label = Label(text="Email/Username : ", bg=colour)
email_label.grid(row=2, column=0, padx=2, pady=2)
pass_digit_label = Label(text="Digits in Password", bg=colour)
pass_digit_label.grid(row=3, column=0, padx=2, pady=2)
password_label = Label(text="Password : ", bg=colour)
password_label.grid(row=4, column=0, padx=2, pady=2)

# Entries

website_entry = Entry(width=32, bg=colour)
website_entry.grid(row=1, column=1, sticky=W)
website_entry.focus()
email_entry = Entry(width=52, bg=colour)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
# email_entry.insert(0, "prashankm5@gmail.com")
pass_digit_entry = Entry(width=32, bg=colour)
pass_digit_entry.grid(row=3, column=1, sticky=W)
password_entry = Entry(width=32, bg=colour)
password_entry.grid(row=4, column=1, sticky=W)

# Buttons
search_button = Button(text="Search", width=15, bg=colour ,command=find_password)
search_button.grid(row=1, column=2, sticky=W)
theme_button = Button(text="Theme", width=15, bg=colour, command=theme)
theme_button.grid(row=3, column=2, sticky=W)
generate_password_button = Button(text="Generate Password", width=15, bg=colour ,command=generate_password)
generate_password_button.grid(row=4, column=2, sticky=W)
add_button = Button(text="Add", width=44, bg=colour, command=save)
add_button.grid(row=5, column=1, columnspan=2, sticky=W)

window.mainloop()

