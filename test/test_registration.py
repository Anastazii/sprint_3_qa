from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurger:
    def test_registration_successfully(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_button')]").click()
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys('Anastasia')
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys('anastasiapopova1090cd sprint9@yandex.ru')
        driver.find_element(By.XPATH, "//div/input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        registration_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']"))).text
        assert registration_button == 'Зарегистрироваться'


    def test_registration_invalid_password(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_button')]").click()
        driver.find_element(By.XPATH, "//a[@href='/register']").click()
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys('Anastasia')
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(By.XPATH, "//div/input[@type='password']").send_keys('12345')
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        error = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text
        assert error == 'Некорректный пароль'



