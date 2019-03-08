#import area
import tkinter
import tkinter as Tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import filedialog
import time

#variables
correct_counter = 0
wrong_counter =0
cards =[]
remaining =60


#functions load_card,next_card,Score

def myOpen():
    myOpen = filedialog.askopenfile("/Cards")
    mlabel4 =Tk.Label(myApp,text=myOpen).pack()

def close_window ():
    window.destroy()
    
global f
f = open("capitals.txt")

def read_question():
    cards=[]
    i = f.readline()
    global a
    q,a = i.split('-')
    qstnarea.config(text = q)
    cards.append([q,a])
    #current_line = current_line + 1
    
def read_answer():
    qstnarea.config(text = a)
    
def correct_guess():
    global correct_counter
    correct_counter += 1
    lab2.config(text= correct_counter)

def wrong_guess():
    global wrong_counter
    wrong_counter += 1
    lab3.config(text= wrong_counter)

def rem_time():
    for i in range(60,0,-1):
        timeshow.config(text = i)


def progress_show():
    window3 = tkinter.Tk()
    window3.geometry("500x400")
    window3.title("Progress")
    Pcorrect1=Tk.Label(window3,text="correct_counter")
    Pcorrect1.pack()
    Pcorrect=Tk.Label(window3,text=correct_counter)
    Pcorrect.pack()
    Pwrong1=Tk.Label(window3, text= "wrong_counter")
    Pwrong1.pack()
    Pwrong=Tk.Label(window3, text= wrong_counter)
    Pwrong.pack()
    window3.mainloop()

#new window
def about():
    window2 = tkinter.Tk()
    window2.geometry("500x400")
    window2.title("About Game")
    label4 = Tk.Label(window2, text="""
A flashcard or flash card is a card bearing information, 
as words or numbers, on either or both sides, used in
 classroom drills or in private study. One writes a question
 on a side and an answer overleaf. Flashcards can bear vocabulary,
 historical dates, formulae or any subject matter that can be
 learned via a question-and-answer format. Flashcards are widely
 used as a learning drill to aid memorization. They are often
 associated with spaced repetition, i.e. reviewed at expanding
 time intervals. """)
    label4.place(x=20, y=20)
    window2.mainloop()

#make the GUI
window = tkinter.Tk()
window.geometry("500x400")
window.title("Flash_card game")

#make frame
windowFrame = Frame(window)
windowFrame.grid(row=5, column=4)


#question area
qstnarea =Tk.Label(window,text=
"""Press Load Card button for
 Load the cards, for next question
 press Next Question button and
 Answer for see the answer""",
                   height=8,width =30, bg="white")
qstnarea.place(x=50, y= 100)
loadcard=Tk.Button(window, text= "Load Card", command=lambda:[read_question(),rem_time()], height =1, width=10)
loadcard.place(x=50, y= 60)
nextqstn=Tk.Button(window, text= "Next Question",command=read_question, height =3, width =10)
nextqstn.place(x=50, y=300)
seeanswr=Tk.Button(window, text= "See Answer",command=read_answer, height =3, width =10)
seeanswr.place(x=190, y=300)


label1=Tk.Label(window, text=" Welcome to FlashCards", font =("Ariel" ,30))
label1.grid(column=0, row=0)

# setting remaining time
remTime=Tk.Label(window, text="Remaining\n Time", height =2, width = 10)
remTime.place(x=350, y =60)
timeshow = Tk.Label(window, height=1, width = 10,bg="white")
timeshow.place(x=350, y= 100)

#corrcet
correct=Tk.Label(window, text="correct\n Guess", height =2, width = 10) #bg="red"
correct.place(x=350, y =140)
lab2 = Tk.Label(window, height=1, width = 10,bg="white")
lab2.place(x=350, y= 180)
btn1 =Tk.Button(window, text= "I Was Right",command=correct_guess, width=10)
btn1.place(x=50, y=250)

#wrong
wrong=Tk.Label(window, text="wrong\n Guess", height =2, width = 10 )
wrong.place(x=350, y =210)
lab3 = Tk.Label(window, height=1, width = 10,bg="white")
lab3.place(x=350, y= 250)
btn2 =Tk.Button(window, text= "I Was Wrong",command=wrong_guess, width =10)
btn2.place(x=190, y=250)

#exit Button
btn3= Tk.Button(window, text="Quit", command=close_window, height=3, width=10)
btn3.place(x=350, y =300)

#New_window
btn4=Tk.Button(window, text= "Show Your Progress",command=progress_show,width = 28)
btn4.place(x=50, y=370)


#create the menubar
menubar =Tk.Menu(window)

#create the file component of that menubar
filemenu = Tk.Menu(menubar, tearoff=0)
filemenu1 =Tk.Menu(menubar, tearoff=0)
#Add the sub headings to the file menu
filemenu.add_command(label="Level", command=myOpen)
menubar.add_cascade(label="File",menu=filemenu)
filemenu1.add_command(label="About Game", command =about)
filemenu.add_command(label="Quit", command =close_window)
menubar.add_cascade(label="About",menu=filemenu1)

#add menubar to the window
window.config(menu=menubar)

window.mainloop()
