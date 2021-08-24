# import Modules
import string
from tkinter import *
from random import choice
import pyperclip

# create wondow
root = Tk()
root.title("PASSWORD-GENERATOR")
root.geometry("325x347")
# bg image
# bg = PhotoImage(file="site-ifca-securite.png")
# Label(root, image=bg).place(x=0, y=0)
Label(root, text="PASSWORD GENERATOR", font="arial 15 bold", fg="green").pack()
Label(root, text="PSSWORD LENGTH", font="arial 10 bold").pack(pady=5)
Label(root, text="idrissi51", font="arial 8").pack(side=BOTTOM)

pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32,
                 textvariable=pass_len, width=15).pack(pady=5)
password = StringVar()


# functions
def generator():
    x = ""
    y = ""
    for z in range(pass_len.get()):
        x = choice(string.ascii_lowercase+string.ascii_uppercase +
                   string.digits+string.punctuation)
        y = y + x
    password.set(y)


def copy():
    pyperclip.copy(password.get())


# button
Button(root, text="GENERATE PASSWORD",
       font="arial 8", command=generator).pack(pady=5)
Entry(root, width=20, textvariable=password).pack(pady=5)
Button(root, text="COPY TO CLIPBOARD", command=copy).pack(pady=5)

# run
root.mainloop()
