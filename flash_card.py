import tkinter
import tkinter as Tk
from tkinter import messagebox

def pop_up():
    msg = messagebox.showinfo( "Hello Python", "Hello World")


    
window = tkinter.Tk()
window.geometry("600x500")
window.title("Flash_card game")

label1=Tk.Label(window, text="welcome to the game", font =("Ariel Bold" ,35))
label1.grid(column=0, row=0)

btn1 =Tk.Button(window, text ="press", command = pop_up)
btn1.place(x=100, y=100)


window.mainloop()
