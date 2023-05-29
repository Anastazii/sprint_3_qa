from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestBurger:
    def test_transfer_to_your_personal_account(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.BUTTON_PERSONAL).click()
        profile = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BUTTON_PROFILE))).text
        assert profile == 'Профиль'
