from selenium.webdriver.common.by import By
from conftest import BASE_URL, ORDER_ENDPOINT
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open_url(BASE_URL)

    def open_order_page(self):
        self.open_url(f"{BASE_URL}{ORDER_ENDPOINT}")

    def wait_for_main_page_url(self):
        self.wait_for_url(BASE_URL)

    # Кнопки заказа
    def click_order_top_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    # Логотипы
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    # Аккордеон
    def get_question_button(self, index):
        buttons = self.get_elements(MainPageLocators.QUESTION_BUTTONS)
        return buttons[index]

    def get_answer_text(self, index):
        answers = self.get_elements(MainPageLocators.ANSWER_TEXTS)
        return answers[index].text

    def wait_for_answer_visible(self, index):
        xpath = f"({MainPageLocators.ANSWER_PANEL_XPATH})[{index+1}]"
        self.wait_for_element_visible((By.XPATH, xpath))

    def close_cookie_banner(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except:
            pass

    def click_question(self, index):
        self.close_cookie_banner()
        button = self.get_question_button(index)
        self.scroll_to_element(button)
        self.click_element_by_element(button)