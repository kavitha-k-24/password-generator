def generate():
    length = int(lenentry.get())
    
    if (length < 8):
        warning = messagebox.askyesno( "Warning" , '''Password length equal to or greater than 8 (recommended).
                            Do you want to change ?''')

        if(warning == True):
            val = StringVar(root , value='')
            lenentry.config(textvariable = val)

        else:  
            password =  ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = length))
            answer = Label(root, text = password , font = ("times new roman bold italic" ,20), bg = "pink" )
            answer.place(x=120, y=200)
            pyperclip.copy(password)
            copied = Label(root, text = "Copied to clipboard" , font = ("times new roman" ,10))
            copied.place(x=120, y=300)

    else:
        password =  ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = length))
        answer = Label(root, text = password , font = ("times new roman bold italic" ,20), bg = "pink" )
        answer.place(x=120, y=200)
        pyperclip.copy(password)
        copied = Label(root, text = "Copied to clipboard" , font = ("times new roman" ,10))
        copied.place(x=120, y=300)

    
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import string , random , pyperclip

root = tk.Tk()
root.configure(bg = "pink")
root.geometry("350x350")
root.resizable(0,0)
root.title("Password Generator")

length = Label(root, text = "Length : " , font = ("times new roman bold italic" ,20), bg = "pink" )
length.place(x=40, y=50)
lenentry = Entry(root, font = ("times new roman bold" ,20), width = 10)
lenentry.place(x=170, y=50)

gen = Button(root, text = "Generate" , font = ("times new roman bold italic" ,20), bg = "red" , fg = "white", command = generate )
gen.place(x=120,y=130)
