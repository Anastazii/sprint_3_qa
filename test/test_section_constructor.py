from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurger:
    def test_go_to_the_sauces_section(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_button')]").click()
        driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]/input").send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(By.XPATH, "//div/input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_size_medium')]").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][1]"))).click()
        test = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").text
        assert test == 'Соусы'

    def test_go_to_the_bread_section(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_button')]").click()
        driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]/input").send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(By.XPATH, "//div/input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_size_medium')]").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][1]"))).click()
        driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][1]").click()
        test = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").text
        assert test == 'Булки'


    def test_go_to_the_fillings_section(self, driver):
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_button')]").click()
        driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text')]/input").send_keys('anastasiapopova10979@yandex.ru')
        driver.find_element(By.XPATH, "//div/input[@type='password']").send_keys('123456')
        driver.find_element(By.XPATH, "//button[contains(@class, 'button_size_medium')]").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][2]"))).click()
        test = driver.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").text
        assert test == 'Начинки'
