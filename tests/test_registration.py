import time
import random

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:
    def test_registration_success(self, driver):
        #переходим на страницу авторизации
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

        #ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        #вводим данные для авторизации
        driver.find_element(By.XPATH, "(.//input)[1]").send_keys("Saya")
        new_email = f"sayatussipbekova3{random.randint(100, 999)}@yandex.ru"
        driver.find_element(By.XPATH, "(.//input)[2]").send_keys(new_email)
        driver.find_element(By.XPATH, "(.//input)[3]").send_keys("123456")
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()

    def test_registration_fail(self, driver):
        #переходим на страницу авторизации
        driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

        #ожидаем загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

        #вводим данные для авторизации
        driver.find_element(By.XPATH, "(.//input)[1]").send_keys("Saya")
        new_email = f"sayatussipbekova3{random.randint(100, 999)}@yandex.ru"
        driver.find_element(By.XPATH, "(.//input)[2]").send_keys(new_email)
        driver.find_element(By.XPATH, "(.//input)[3]").send_keys("12345")
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()

        error_text = driver.find_element(By.CSS_SELECTOR, ".input__error").text

        # проверяем что текст ошибки равен 'Некорректный пароль'
        assert error_text == 'Некорректный пароль'



