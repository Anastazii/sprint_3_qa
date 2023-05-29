from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestBurger:
    def test_sing_in_to_account_button_successfully(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_ORDER))).text
        assert text == 'Оформить заказ'


    def test_login_via_your_personal_account_successfully(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.REG_BUTTON1).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_ORDER))).text
        assert text == 'Оформить заказ'


    def test_login_via_the_button_in_the_registration_form(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.BUTTON_SING_IN).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.REG_BUTTON1).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_ORDER))).text
        assert text == 'Оформить заказ'

    def test_login_via_the_button_in_the_password_recovery_form(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(*Locators.BUTTON_RESTORE_PASSWORD).click()
        driver.find_element(*Locators.BUTTON_SING_IN).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.REG_BUTTON1).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_ORDER))).text
        assert text == 'Оформить заказ'
