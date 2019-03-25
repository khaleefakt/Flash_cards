#import flshlib
import tkinter as Tk
import random

def load_cards(fname):
    cards = {}
    with open(fname) as f:
        for i in f:
            i = i.strip()
            q, a = i.split(" - ")
            cards[q] = a
    return cards
def loadcards(cards, qstnarea):
    ques = list(cards.keys())
    qstnarea.config(text=ques[0])
def destroy_button(buttonload):
    buttonload.destroy()

def get_answer_for_qn(cards, qn):
    return cards[qn]
def get_answer(cards, qn,qstnarea):
    ans = list(cards.values())
    qstnarea.config(text=ans[0])
def ans_frame(window,cards,qn,qstnarea):
    seeanswr= Tk.Button(window, name="show_answer", text ="Show Answer", command=get_answer(cards,qn,qstnarea), height = 2, width = 30)
    seeanswr.place(x=20,y=250)


    
def get_next_card(cards):
    return random.choice(list(cards))

    
def main():    
    window = Tk.Tk()
    window.geometry("300x400")
    window.title("Simple Flash Card")


    cards = load_cards("test_card.txt")
    # state = create_scores()
    qn = get_next_card(cards)

    qstnarea = Tk.Label(window,  text="", height=8, width=33, bg="white")
    qstnarea.place(x=20,y=60)
    buttonload= Tk.Button(window, name="load_Button", text ="Load Card",
                          command=lambda:[loadcards(cards,qstnarea),
                                          destroy_button(buttonload),
                                          ans_frame(window,cards,qn,qstnarea)])
    buttonload.place(x=20,y=20)

  
    window.mainloop()

    
main()


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



# import random

# def create_scores():
#     return dict(right = 0,
#                 wrong = 0)

        
# def load_cards(fname):
#     cards = {}
#     with open(fname) as f:
#         for i in f:
#             i = i.strip()
#             q, a = i.split(" - ")
#             cards[q] = a
#     return cards

# def get_next_card(cards):
#     return random.choice(list(cards))

# def get_answer_for_qn(cards, qn):
#     return cards[qn]

# def process_right_answer(scores):
#     scores['right'] += 1

# def process_wrong_answer(scores):
#     scores['wrong'] += 1




        




