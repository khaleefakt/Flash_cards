import tkinter
import tkinter as Tk


window = tkinter.Tk()
window.geometry("600x500")
window.title("Flash_card game")
label1=Tk.Label(window, text="welcome to the game", font =("Ariel Bold" ,35))
label1.grid(column=0, row=0)

window.mainloop()

