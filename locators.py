from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button')]") #кнопка войти в аккаунт
    REG_BUTTON = (By.XPATH, "//a[@href='/register']") #кнопка Зарегистрироваться
    NAME = (By.XPATH, "//fieldset[1]/div/div/input[@name='name']") #поле Имя
    EMAIL_REG = (By.XPATH, "//fieldset[2]/div/div/input[@name='name']") # поле email для регистрации
    EMAIL = (By.XPATH, "//input[@name='name']") #почта для входа
    PASSWORD = (By.XPATH, "//input[@type='password']") # поле Пароль
    REG_BUTTON1 = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # кнопка Зарегистрироваться
    INCORRECT_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default']") # ошибка Некорректный пароль
    BUTTON_LOGIN = (By.XPATH, "//button[contains(@class, 'button_size_medium')]") # Кнопка Войти на главной странице
    BUTTON_ORDER = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # кнопка Оформить заказ
    BUTTON_PERSONAL = (By.XPATH, "//a[@href='/account']") # кнопка Личный кабинет
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']") # кнопка Восстановить пароль
    BUTTON_SING_IN = (By.XPATH, "//a[@href='/login']") # кнопка Войти
    BUTTON_PROFILE = (By.XPATH, "//a[@href='/account/profile']") # кнопка Профиль
    BUTTON_EXIT = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']") # кнопка Выход
    CONSTRUCTOR = (By.XPATH, "//a[@href='/' and @class]") # вкладка Конструктор
    LOGO = (By.XPATH, "//a[@href='/']") # Логотип
    UNOPEN_TAB1 = (By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][1]")# первая неоткрытая вкладка( соусы и тд)
    OPEN_TAB = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']") # открытая вкладка (булки и тд)
    UNOPEN_TAB2 = (By.XPATH, "//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'][2]") # вторая неоткрытая вкладка (начинки)