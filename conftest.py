import pytest
from selenium import webdriver

url = 'https://stellarburgers.nomoreparties.site'


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()