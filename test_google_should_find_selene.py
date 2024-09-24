import pytest
from selene import browser, be, have


@pytest.fixture()
def open_page(firefox_browser_actions):
    browser.open('https://google.com')


# Поиск выдает результаты по запросу
def test_google_should_find_selene_positive(open_page):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


# Поиск не выдает результатов по запросу и пишет сообщение
def test_google_should_find_selene_negative(open_page):
    random_string = 'fsdsdfsdfsdfsdfsdsdfsdfsd'
    browser.element('[name="q"]').should(be.blank).type(random_string).press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу ' + random_string + ' ничего не найдено.'))
