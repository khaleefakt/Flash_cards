import tkinter
import tkinter as Tk
from tkinter import messagebox

def pop_up():
    msg = messagebox.showinfo( "Hello Python", "Hello World")

def read_questions():
    with open("test_card.txt") as f:
        for line in f:
            a = line.split()
            que = a[0]
            ans = a[1] 
            print("question {} answer {}".format(que,ans))

def close_window (): 
    window.destroy()

window = tkinter.Tk()
window.geometry("500x400")
window.title("Flash_card game")




label1=Tk.Label(window, text=" welcome to FlashCards", font =("Ariel" ,30))
label1.grid(column=0, row=0)

# setting remaining time
remTime=Tk.Label(window, text="Remaining\n Time", height =2, width = 10)
remTime.place(x=350, y =50)
text1 = Tk.Text(window, height=2, width = 10)
text1.place(x=350, y= 100)

#corrcet
correct=Tk.Label(window, text="corrected", height =3, width = 10)
correct.place(x=350, y =120)
text2 = Tk.Text(window, height=2, width = 10)
text2.place(x=350, y= 170)

#wrong
wrong=Tk.Label(window, text="wrong", height =3, width = 10 )
wrong.place(x=350, y =200)
text3 = Tk.Text(window, height=2, width = 10)
text3.place(x=350, y= 250)

#exit Button
btn3= Tk.Button(window, text="Quit", command=close_window, height=3, width=10)
btn3.place(x=350, y =310)

window.mainloop()
