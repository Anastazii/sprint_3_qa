from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestBurger:
    def test_registration_successfully(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys('Anastasia')
        driver.find_element(*Locators.EMAIL_REG).send_keys('anastasiapopova10959@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.REG_BUTTON1).click()
        registration_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Locators.REG_BUTTON))).text
        assert registration_button == 'Зарегистрироваться'


    def test_registration_invalid_password(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys('Anastasia')
        driver.find_element(*Locators.EMAIL_REG).send_keys('anastasiapopova10959@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON1).click()
        error = driver.find_element(*Locators.INCORRECT_PASSWORD).text
        assert error == 'Некорректный пароль'
