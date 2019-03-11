import flash_card_simple

def test_close_window():
    window = MainFrame
    assert window == window.destroy
def test_read_qstn():
    window = MainFrame()
    button = window.nametowidget("window.load_card")
    label = window.nametowidget("window.qstnarea")
    assert label.cget('text') == "Brazil"
    button.invoke()
    assert label.cget('text') == "Bulgaria"
