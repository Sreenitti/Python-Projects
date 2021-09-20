from tkinter import *
import bcrypt
 
def validate(password) :
    hash = b'$2b$12$BZUGjfdcn5nhT9JS4JOMOuWIPlI/vfX0sZ0olbCCOj8BIkTmR3k4q'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash) :
        print("Login successful")
    else :
        print("Incorrect password")




root = Tk ()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="Validate", command=lambda : validate(password_entry.get()))
button.pack()

root.mainloop()