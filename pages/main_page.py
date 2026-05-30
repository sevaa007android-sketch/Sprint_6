from conftest import DEFAULT_TIMEOUT
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы кнопок заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]/button[contains(@class, 'Button_Button') and text()='Заказать']")    
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button') and text()='Заказать']")

    # Локаторы логотипов
    SCOOTER_LOGO = (By.XPATH, "//a[.//img[@alt='Scooter']]")
    YANDEX_LOGO = (By.XPATH, "//a[.//img[@alt='Yandex']]")

    # Локаторы аккордеона и куки
    QUESTION_BUTTONS = (By.XPATH, "//div[@class='accordion__button']")
    ANSWER_TEXTS = (By.XPATH, "//div[@class='accordion__panel']")
    ANSWER_PANEL_XPATH = "//div[@class='accordion__panel']"
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # Методы для логотипов и переключения окон 
    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()

    def switch_to_new_window(self):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # Методы для аккордеона 
    def get_question_button(self, index):
        buttons = self.driver.find_elements(*self.QUESTION_BUTTONS)
        return buttons[index]

    def get_answer_text(self, index):
        answers = self.driver.find_elements(*self.ANSWER_TEXTS)
        return answers[index].text

    def wait_for_answer_visible(self, index):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located((By.XPATH, f"({self.ANSWER_PANEL_XPATH})[{index+1}]"))
        )

    def close_cookie_banner(self):
        try:
            cookie_button = self.driver.find_element(*self.COOKIE_BUTTON)
            cookie_button.click()
        except:
            pass

    def click_question(self, index):
        self.close_cookie_banner()
        button = self.get_question_button(index)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.3)
        button.click()

    def click_order_top_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_TOP).click()

    def click_order_bottom_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_BOTTOM).click()