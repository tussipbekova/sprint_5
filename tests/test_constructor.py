import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    def test_constructor_nachinki(self, driver, email, password, main_page_url):
        # Клик на Личный кабинет
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # Выполняем авторизацию
        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        # вход в «Личный Кабинет»
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))
        # клик по кнопке «Конструктор»
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

        # Нашли карточку раздела и сделали скролл до неё
        element = driver.find_element(By.XPATH, ".//h2[text()='Начинки']")
        driver.execute_script("arguments[0].scrollIntoView();", element)

        # Проверяем, что текущий url равен  main_page_url
        assert driver.current_url == main_page_url

    def test_constructor_sousy(self, driver, email, password, main_page_url):
        # Клик на Личный кабинет
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # Выполняем авторизацию
        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        # вход в «Личный Кабинет»
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))

        # переход по клику на "Конструктор"
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

        # Найди карточку контента и сделай скролл до неё
        element = driver.find_element(By.XPATH, ".//h2[text()='Соусы']")
        driver.execute_script("arguments[0].scrollIntoView();", element)

        # Проверяем, что текущий url равен  main_page_url
        assert driver.current_url == main_page_url


    def test_constructor_bulki(self, driver, email, password, main_page_url):
        # Клик на Личный кабинет
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # Выполняем авторизацию
        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        # вход в «Личный Кабинет»
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))

        # переход по клику на "Конструктор"
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

        # Найди карточку контента и сделай скролл до неё
        element = driver.find_element(By.XPATH, ".//h2[text()='Булки']")
        driver.execute_script("arguments[0].scrollIntoView();", element)

        # Проверяем, что текущий url равен  main_page_url
        assert driver.current_url == main_page_url