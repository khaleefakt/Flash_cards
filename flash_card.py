import tkinter
import tkinter as Tk
from tkinter import messagebox

def pop_up():
    msg = messagebox.showinfo( "Hello Python", "Hello World")

def open_card():
    f = open("card.txt","r")
    f1 = f.readline()
    for x in f1:
        print (x)

def close_window (): 
    window.destroy()

    
window = tkinter.Tk()
window.geometry("600x500")
window.title("Flash_card game")

label1=Tk.Label(window, text="welcome to the game", font =("Ariel Bold" ,35))
label1.grid(column=0, row=0)

btn1 =Tk.Button(window, text ="press", command = pop_up)
btn1.place(x=100, y=100)

btn2 =Tk.Button(window, text ="read card", command = open_card)
btn2.place(x=200, y=200)

btn3= Tk.Button(window, text="Quit", command=close_window)
btn3.place(x=250, y =200)

window.mainloop()
