import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    def test_constructor_nachinki(self, driver, email, password, main_page_url):
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

        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

        # Найди карточку контента и сделай скролл до неё
        element = driver.find_element(By.XPATH, ".//h2[text()='Начинки']")
        driver.execute_script("arguments[0].scrollIntoView();", element)


        assert driver.current_url == main_page_url

    def test_constructor_sousy(self, driver, email, password, main_page_url):
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

        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

        # Найди карточку контента и сделай скролл до неё
        element = driver.find_element(By.XPATH, ".//h2[text()='Соусы']")
        driver.execute_script("arguments[0].scrollIntoView();", element)


        assert driver.current_url == main_page_url


    def test_constructor_bulki(self, driver, email, password, main_page_url):
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

        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

        # Найди карточку контента и сделай скролл до неё
        element = driver.find_element(By.XPATH, ".//h2[text()='Булки']")
        driver.execute_script("arguments[0].scrollIntoView();", element)


        assert driver.current_url == main_page_url