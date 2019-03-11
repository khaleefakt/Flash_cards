import random

def create_scores():
    return dict(right = 0,
                wrong = 0)

        
def load_cards(fname):
    cards = {}
    with open(fname) as f:
        for i in f:
            i = i.strip()
            q, a = i.split(" - ")
            cards[q] = a
    return cards

def get_next_card(cards):
    return random.choice(list(cards))

def get_answer_for_qn(cards, qn):
    return cards[qn]

def process_right_answer(scores):
    scores['right'] += 1

def process_wrong_answer(scores):
    scores['wrong'] += 1




        
