#import area
import tkinter
import tkinter as Tk
from tkinter import messagebox
#variables
correct_counter = 0
wrong_counter =0
#functions
def pop_up():
    msg = messagebox.showinfo( "Confirmation", "Are You Sure..?")

def read_questions():
    with open("test_card.txt") as f:
        for line in f:
            a = line.split()
            que = a[0]
            ans = a[1]
            qstnarea.config(text=que)
            #print("question {} answer {}".format(que,ans))

def read_answer():
    with open("test_card.txt") as f:
        for line in f:
            a = line.split()
            que = a[0]
            ans = a[1]
            qstnarea.config(text=ans)
            #print("question {} answer {}".format(que,ans))

def close_window ():
    window.destroy()

def correct_guess():
    global correct_counter
    correct_counter += 1
    lab2.config(text= correct_counter)

def wrong_guess():
    global wrong_counter
    wrong_counter += 1
    lab3.config(text= wrong_counter)


window = tkinter.Tk()
window.geometry("500x400")
window.title("Flash_card game")

#question area
qstnarea =Tk.Label(window,text="",height=8,width =30, bg="white")
qstnarea.place(x=50, y= 100)
nextqstn=Tk.Button(window, text= "Next Question",command=read_questions, height =3, width =10)
nextqstn.place(x=60, y=300)
seeanswr=Tk.Button(window, text= "See Answer",command=read_answer, height =3, width =10)
seeanswr.place(x=200, y=300)


label1=Tk.Label(window, text=" welcome to FlashCards", font =("Ariel" ,30))
label1.grid(column=0, row=0)

# setting remaining time
remTime=Tk.Label(window, text="Remaining\n Time", height =2, width = 10)
remTime.place(x=350, y =50)
lab1 = Tk.Label(window, height=2, width = 10,bg="white")
lab1.place(x=350, y= 100)

#corrcet
correct=Tk.Label(window, text="corrected", height =3, width = 10,bg="red")
correct.place(x=350, y =120)
lab2 = Tk.Label(window, height=2, width = 10,bg="white")
lab2.place(x=350, y= 170)
btn1 =Tk.Button(window, text= "I Was Right",command=lambda:[correct_guess(),pop_up()])
btn1.place(x=50, y=250)

#wrong
wrong=Tk.Label(window, text="wrong", height =3, width = 10 )
wrong.place(x=350, y =200)
lab3 = Tk.Label(window, height=2, width = 10,bg="white")
lab3.place(x=350, y= 250)
btn2 =Tk.Button(window, text= "I Was Wrong",command=lambda:[ wrong_guess(),pop_up()])
btn2.place(x=170, y=250)

#exit Button
btn3= Tk.Button(window, text="Quit", command=close_window, height=3, width=10)
btn3.place(x=350, y =310)


window.mainloop()
