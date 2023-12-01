import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:
    def test_login_through_login_to_account(self, driver, email, password, main_page_url):
        #нашли кнопку "Войти в аккаунт" и клик по ней
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # выполняем авторизацию
        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы с кнопкой 'Оформить заказ'
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        #проверяем соответствие url
        assert driver.current_url == main_page_url

    def test_login_through_personal_account(self, driver, email, password, main_page_url):
        # клик по кнопке "Личный кабинет"
        driver.find_element(By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']//p[text()='Личный Кабинет']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # выполняеи авторизацию
        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы 'Оформить заказ'
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        # проверяем соответствие url
        assert driver.current_url == main_page_url


    def test_login_through_registration(self,driver, email, password, main_page_url):
        # клик по кнопке "Личный кабинет"
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # клик по кнопке "Зарегистрироваться"
        driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # клик по кнопке "Войти"
        driver.find_element(By.XPATH,".//a[text()='Войти']").click()

        # вводим входные данные
        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы с кнопкой 'Оформить заказ'
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        # проверяем соответствие url
        assert driver.current_url == main_page_url


    def test_login_through_restore_password(self,driver, email, password, main_page_url):
        # клик по кнопке "Личный кабинет"
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # клик по кнопке "Восстановить пароль"
        driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']").click()

        # ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        # клик по кнопке "Войти"
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()

        # вводим входные данные
        driver.find_element(By.NAME, "name").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()

        # ожидаем загрузки страницы с кнопкой 'Оформить заказ'
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        # проверяем соответствие url
        assert driver.current_url == main_page_url


