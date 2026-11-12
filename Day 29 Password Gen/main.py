from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    pw = pw_entry.get()

    if len(pw) == 0 or website == 0:
        messagebox.showinfo(title="warning",  message="Don't leave any empty fields")

    else:
        is_saved = messagebox.askokcancel(title=website, message=f"Email: {email} \n"
                                                      f"Password: {pw} \n"
                                                      f"Okay to save?")
        if is_saved:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email} | {pw}\n")
                website_entry.delete(0, END)
                pw_entry.delete(0, END)






# # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width = 200, height = 200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "DEFAULT EMAIL VALUE")
pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1)

pw_button = Button(text="Generate Password")
pw_button.grid(row=3, column=2, )
pw_button = Button(text="Add", width=40, command=save)
pw_button.grid(row=4, column=1,columnspan=2 )



window.mainloop()