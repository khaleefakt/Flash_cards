import tkinter as Tk
 #----------------------------------------------------------------------

global f
f = open("capitals.txt")
#variables
correct_counter = 0
wrong_counter = 0
remaining = 60

#-------------------------------------------------------------------------
def MainFrame():
    def close_window():
        window.destroy()
    def load_card():
        Button.loadcard.destroy()
        cards = []
        i = f.readline()
        global a
        q, a = i.split('-')
        qstnarea.config(text=q)
        cards.append([q, a])
    def read_question():
        cards = []
        i = f.readline()
        global a
        q, a = i.split('-')
        qstnarea.config(text=q)
        cards.append([q, a])
        #current_line = current_line + 1
    def read_answer():
        qstnarea.config(text=a)
    def answer_button():
        #nextqstn.destroy()
        seeanswr = Tk.Button(window, name="see_answr", text= "See Answer",
                             command=lambda:[read_answer(),score(next_qstn_btn,seeanswr)], height=3, width=30)
        seeanswr.place(x=40, y=250)
    def correct_guess():
        global correct_counter
        correct_counter += 1
        lab2.config(text=correct_counter)
    def wrong_guess():
        global wrong_counter
        wrong_counter += 1
        lab3.config(text=wrong_counter)
    def next_qstn_btn(seeanswr,btn1,btn2):
        seeanswr.destroy()
        btn1.destroy()
        btn2.destroy()
        nextqstn = Tk.Button(window, name="next_qstn", text="Next Question",
                             command=lambda:[read_question(),answer_button()], height=3, width=30)
        nextqstn.place(x=40, y=250)
    def score(next_qstn_btn,seeanswr):
        seeanswr.destroy()
        btn1 = Tk.Button(window, name="correct_guess", text="I Was Right",
                         command=lambda:[correct_guess(),next_qstn_btn(seeanswr,btn1,btn2)], width=14,height=3)
        btn1.place(x=40, y=250)
        btn2 = Tk.Button(window, name="wrong_guess", text="I Was Wrong",
                         command=lambda:[wrong_guess(),next_qstn_btn(seeanswr,btn1,btn2)], width=14,height=3)
        btn2.place(x=170, y=250)
    def disable():
        loadcard.destroy()
    def restart():
        MainFrame()
        window.destroy()
 #----------------------------------------------------------------------------------------------
    window = Tk.Tk()
    window.geometry("350x500")
    window.title("Flash_card game")
    #question area
    qstnarea = Tk.Label(window, name="qstnarea", text=
                    """Press Load Card button for
    Load the cards, for next question
    press Next Question button and
    Answer for see the answer""",
                        height=8, width=30, bg="white")
    qstnarea.place(x=40, y=100)
 
    loadcard = Tk.Button(window, name="load_card", text="Load Card",
                         command=lambda:[read_question(),answer_button(),disable()], height=1, width=10)
    loadcard.place(x=50, y=60)
 
    #corrcet
    correct = Tk.Label(window, text="correct\n Guess", height=2, width=10) #bg="red"
    correct.place(x=20, y =330)
    lab2 = Tk.Label(window,text='0', height=2, width=5,bg="white")
    lab2.place(x=100, y=330)
    wrong = Tk.Label(window, text="wrong\n Guess", height=2, width=10 )
    wrong.place(x=150, y=330)
    lab3 = Tk.Label(window,text='0', height=2, width=5, bg="white")
    lab3.place(x=230, y=330)
    #exit Button
    btn3 = Tk.Button(window, text="Quit", command=close_window, height=3, width=10)
    btn3.place(x=350, y=300)
    btnclr = Tk.Button(window, text="Restart", command=restart, height=1, width=10)
    btnclr.place(x=350, y=5)
    return window
#----------------------------------------------------------------------------------------------
def main():
    window = MainFrame()
    window.mainloop()
#------------------------------------------------------------------
if __name__ == "__main__":
    main()
#----------------------------------------------------------------------
