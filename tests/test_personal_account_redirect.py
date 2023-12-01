import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalAccountRedirect:
    def test_personal_account_redirect_to_constructor(self, driver, email, password, main_page_url):
        # клик по кнопке "Личный кабинет"
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # выполняем авторизацию
        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        # клик по кнопке "Личный кабинет"
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))

        # клик по кнопке "Конструктор"
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

        # Проверяем, что текущий url равен  main_page_url
        assert driver.current_url == main_page_url

    def test_personal_account_redirect_to_stellar_burgers(self, driver, email, password, main_page_url):
        # клик по кнопке "Личный кабинет"
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # выполняем авторизацию
        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        # клик по кнопке "Личный кабинет"
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))

        # клик по логотипу "Stellar Burger"
        driver.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']//a").click()

        # Проверяем, что текущий url равен  main_page_url
        assert driver.current_url == main_page_url
