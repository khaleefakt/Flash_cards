from flashlib import *

def main():
    cards = load_cards('test_card.txt')
    state = create_scores()
    while True:
        print ("Right {} Wrong {}".format(state['right'], state['wrong']))
        card = get_next_card(cards)
        print (card)
        input("Show answer")
2        print  ("Answer is {}".format(get_answer_for_qn(cards,  card)))
        rw = input("r or w?")
        if rw == 'r':
            process_right_answer(state)
        else:
            process_wrong_answer(state)
                
    

if __name__ == "__main__":
    main()
