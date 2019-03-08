#import area
import tkinter
import tkinter as Tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import filedialog

#variables
correct_counter = 0
wrong_counter =0
cards =[]
remaining =60


#functions load_card,next_card,Score
def remTime():
    global remainig
    if remaining <= 0:
        lab1.config(text="Times Up.")
    else:
        for i in remaining:
            lab1.config(text=remaining)
            remaining = remaining - 1


def pop_up():
    msg = messagebox.showinfo( "Confirmation", "Are You Sure..?")

def myOpen():
    myOpen = filedialog.askopenfile("/Cards")
    mlabel4 = Label(myApp,text=myOpen).pack()

def close_window ():
    window.destroy()


    
global f
f = open("capitals.txt")
def call_back():
    loadcard.config(state = DISABLED)
def read_question():
    cards=[]
    i = f.readline()
    global a
    q,a = i.split('-')
    qstnarea.config(text = q)
    cards.append([q,a])
    #current_line = current_line + 1
    
def read_answer():
    ans = a
    qstnarea.config(text = ans)
    

def correct_guess():
    global correct_counter
    correct_counter += 1
    lab2.config(text= correct_counter)

def wrong_guess():
    global wrong_counter
    wrong_counter += 1
    lab3.config(text= wrong_counter)


#new window
def about():
    window2 = tkinter.Tk()
    window2.geometry("500x400")
    window2.title("New Window")
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


chk = Tk.Checkbutton(window, text="pic")

#question area
qstnarea =Tk.Label(window,text=
"""Press Load Card button for
 Load the cards, for next question
 press Next Question button and
 Answer for see the answer""",
                   height=8,width =30, bg="white")
qstnarea.place(x=50, y= 100)
loadcard=Tk.Button(window, text= "Load Card", command=lambda:[read_question(),call_back()], height =1, width=10, state= DISABLE)
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
lab1 = Tk.Label(window, height=1, width = 10,bg="white")
lab1.place(x=350, y= 100)

#corrcet
correct=Tk.Label(window, text="correct\n Guess", height =2, width = 10) #bg="red"
correct.place(x=350, y =140)
lab2 = Tk.Label(window, height=1, width = 10,bg="white")
lab2.place(x=350, y= 180)
btn1 =Tk.Button(window, text= "I Was Right",command=lambda:[correct_guess(),pop_up()], width=10)
btn1.place(x=50, y=250)

#wrong
wrong=Tk.Label(window, text="wrong\n Guess", height =2, width = 10 )
wrong.place(x=350, y =210)
lab3 = Tk.Label(window, height=1, width = 10,bg="white")
lab3.place(x=350, y= 250)
btn2 =Tk.Button(window, text= "I Was Wrong",command=lambda:[wrong_guess(),pop_up()], width =10)
btn2.place(x=190, y=250)

#exit Button
btn3= Tk.Button(window, text="Quit", command=close_window, height=3, width=10)
btn3.place(x=350, y =300)

#New_window
#btn4=Tk.Button(window, text= "New window",command=command)
#btn4.place(x=190, y=280)


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
