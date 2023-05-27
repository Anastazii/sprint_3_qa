from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurger:
    def test_transfer_to_your_personal_account(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_button')]").click()
        driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]/input").send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(By.XPATH, "//div/input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_size_medium')]").click()
        driver.find_element(By.XPATH, "//a[@href='/account']").click()
        profile = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/account/profile']"))).text
        assert profile == 'Профиль'
