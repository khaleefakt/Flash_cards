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
current_card = 0
#functions
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

def next_card():
    with open("test_card.txt") as f:
        for i in f: #1
            q,a=i.split('-') #2
            cards.append([q,a]) #3
            qstnarea.config(text =q)
    
    
            
#def next_card():
 #   cards[q]=q
   # card[q] +=1
  #  qstnarea.config(text=q)
    
def read_answer():
    with open("test_card.txt") as f:
        for i in f:
            q,a=i.split('-')
            cards.append([q,a])
            qstnarea.config(text=a)
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

#new window
def about():
    window2 = tkinter.Tk()
    window2.geometry("500x400")
    window2.title("New Window")
    label4 = Tk.Label(window2, text="This is the new window")
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
qstnarea =Tk.Label(window,text="",height=8,width =30, bg="white")
qstnarea.place(x=50, y= 100)
nextqstn=Tk.Button(window, text= "Next Question",command=next_card, height =3, width =10)
nextqstn.place(x=50, y=300)
seeanswr=Tk.Button(window, text= "See Answer",command=read_answer, height =3, width =10)
seeanswr.place(x=190, y=300)


label1=Tk.Label(window, text=" welcome to FlashCards", font =("Ariel" ,30))
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
filemenu1.add_command(label="About us", command =about)
menubar.add_cascade(label="About",menu=filemenu1)

#add menubar to the window
window.config(menu=menubar)

window.mainloop()
