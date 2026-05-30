from conftest import DEFAULT_TIMEOUT
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы формы заказа (первая страница)
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    FIRST_METRO_OPTION = (By.XPATH, "//div[@class='select-search__select']//li")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы второй страницы (дата, аренда, цвет)
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # Кнопка подтверждения и сообщение об успехе
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # Методы для заполнения первой страницы
    def fill_name(self, name):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)

    def fill_surname(self, surname):
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)

    def fill_address(self, address):
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)

    def fill_metro(self, metro_station):
        self.driver.find_element(*self.METRO_FIELD).click()
        time.sleep(0.5)
        metro_input = self.driver.find_element(*self.METRO_FIELD)
        metro_input.clear()
        metro_input.send_keys(metro_station)
        time.sleep(0.5)
        first_option = WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(self.FIRST_METRO_OPTION)
        )
        first_option.click()

    def fill_phone(self, phone):
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    # Методы для второй страницы
    def fill_date(self, date):
        self.driver.find_element(*self.DATE_FIELD).send_keys(date)
        # Клик по другому элементу, чтобы закрыть календарь
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def select_rental_period(self, period_text):
        self.driver.find_element(*self.RENTAL_PERIOD_FIELD).click()
        time.sleep(0.5)
        options = self.driver.find_elements(*self.RENTAL_OPTIONS)
        for option in options:
            if period_text.lower() in option.text.lower():
                option.click()
                break

    def select_color(self, color):
        if color == "black":
            self.driver.find_element(*self.COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*self.COLOR_GREY).click()

    def click_order(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def confirm_order(self):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        ).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text

    # Универсальный метод заполнения всей формы 
    def fill_order_form(self, data):
        self.fill_name(data["name"])
        self.fill_surname(data["surname"])
        self.fill_address(data["address"])
        self.fill_metro(data["metro"])
        self.fill_phone(data["phone"])
        self.click_next()
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(self.DATE_FIELD)
        )
        self.fill_date(data["date"])
        self.select_rental_period(data["rental_period"])
        self.select_color(data["color"])
        self.click_order()
        self.confirm_order()