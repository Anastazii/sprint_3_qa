from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurger:
    def test_transfer_from_personal_account_by_clicking_on_the_Constructor(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_button')]").click()
        driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]/input").send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(By.XPATH, "//div/input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_size_medium')]").click()
        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        driver.find_element(By.XPATH, "//a[@href='/' and @class]").click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"))).text
        assert text == 'Оформить заказ'



    def test_transfer_from_your_personal_account_by_clicking_on_the_logo(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_button')]").click()
        driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]/input").send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(By.XPATH, "//div/input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_size_medium')]").click()
        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        driver.find_element(By.XPATH, "//div/a[@href='/']").click()
        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"))).text
        assert text == 'Оформить заказ'


