from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]/button[contains(@class, 'Button_Button') and text()='Заказать']")    
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button') and text()='Заказать']")

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[.//img[@alt='Scooter']]")
    YANDEX_LOGO = (By.XPATH, "//a[.//img[@alt='Yandex']]")

    # Аккордеон
    QUESTION_BUTTONS = (By.XPATH, "//div[@class='accordion__button']")
    ANSWER_TEXTS = (By.XPATH, "//div[@class='accordion__panel']")
    ANSWER_PANEL_XPATH = "//div[@class='accordion__panel']"

    # Куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")