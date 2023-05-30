from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestBurger:
    def test_go_to_the_sauces_section(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.UNOPEN_TAB1))).click()
        test = driver.find_element(*Locators.OPEN_TAB).text
        assert test == 'Соусы'

    def test_go_to_the_bread_section(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.UNOPEN_TAB1))).click()
        driver.find_element(*Locators.UNOPEN_TAB1).click()
        test = driver.find_element(*Locators.OPEN_TAB).text
        assert test == 'Булки'


    def test_go_to_the_fillings_section(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.UNOPEN_TAB2))).click()
        test = driver.find_element(*Locators.OPEN_TAB).text
        assert test == 'Начинки'
