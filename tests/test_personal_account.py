import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalAccount:
    def test_personal_account(self, driver, email, password):
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
