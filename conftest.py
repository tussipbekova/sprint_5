import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()  # Or any other browser
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver

    driver.quit()

@pytest.fixture()
def email():
    return 'sayatussipbekova3888@yandex.ru'

@pytest.fixture()
def password():
    return "123456"

@pytest.fixture()
def main_page_url():
    return 'https://stellarburgers.nomoreparties.site/'
