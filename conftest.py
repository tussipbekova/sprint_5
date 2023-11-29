import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()  # Or any other browser
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver

    driver.quit()