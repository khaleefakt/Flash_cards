#import flshlib
import tkinter as Tk


def load_cards():
    buttonload.destroy()
    fname = "test_card.txt"
    cards = {}
    with open(fname) as f:
        for i in f:
            i = i.strip()
            q, a = i.split(" - ")
            cards[q] = a
    qstnarea.config(text=cards[q])


window = Tk.Tk()
window.geometry("300x400")
window.title("Simple Flash Card")


#cards = load_cards()
#state = create_scores()

qstnarea = Tk.Label(window,  text="", height=8, width=33, bg="white")
qstnarea.place(x=20,y=60)
buttonload= Tk.Button(window, name="load_Button", text ="Load Card",command=load_cards)
buttonload.place(x=20,y=20)



# f1 = Tk.Frame(name='frame', bg="white", height = 4, width=33)
# f1.place(x=20, y=250)
# l = Tk.Label(f1, name="card_label")
# l.pack()

window.mainloop()
# def main():
#     cards = load_cards('test_card.txt')
#     state = create_scores()
#     while True:
#         print ("Right {} Wrong {}".format(state['right'], state['wrong']))
#         card = get_next_card(cards)
#         print (card)
#         input("Show answer")
#         print  ("Answer is {}".format(get_answer_for_qn(cards,  card)))
#         rw = input("r or w?")
#         if rw == 'r':
#             process_right_answer(state)
#         else:
#             process_wrong_answer(state)
                
    

# if __name__ == "__main__":
#     main()





