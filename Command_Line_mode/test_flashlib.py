import flashlib

def test_create_score():
    assert flashlib.create_scores() == {'right': 0, 'wrong' : 0}

def test_load_cards():
    fname = "test_small.txt"
    assert flashlib.load_cards(fname) == {'Bhutan': 'Thimphu', 'Botswana': 'Gaborone'}

def test_next_card():
    cards= {'Bhutan' : 'Thimphu'}
    assert flashlib.get_next_card(cards) == "Bhutan"

def test_answer_for_qstn():
    cards = {'Bhutan' : 'Thimphu'}
    qn = "Bhutan"
    assert flashlib.get_answer_for_qn(cards, qn) == "Thimphu"
    

