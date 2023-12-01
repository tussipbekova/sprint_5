import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = "../chromedriver"


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def email():
    return 'sayatussipbekova3888@yandex.ru'

@pytest.fixture(scope="function")
def password():
    return "123456"

@pytest.fixture(scope="function")
def main_page_url():
    return 'https://stellarburgers.nomoreparties.site/'
