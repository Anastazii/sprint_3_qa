from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestBurger:
    def test_transfer_from_personal_account_by_clicking_on_the_Constructor(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_ORDER))).text
        assert text == 'Оформить заказ'



    def test_transfer_from_your_personal_account_by_clicking_on_the_logo(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        driver.find_element(*Locators.LOGO).click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_ORDER))).text
        assert text == 'Оформить заказ'


