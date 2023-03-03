from selene.support.shared import browser
from selene import be, have

def test_find_google(window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_find_google(window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('738е2нву73ав73е4уаащщщщщ').press_enter()
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено.'))

