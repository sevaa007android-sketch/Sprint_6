from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Первая страница
    def fill_name(self, name):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name)

    def fill_surname(self, surname):
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname)

    def fill_address(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)

    def fill_metro(self, metro_station):
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.clear_and_send_keys(OrderPageLocators.METRO_FIELD, metro_station)
        self.click_element(OrderPageLocators.FIRST_METRO_OPTION)

    def fill_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD, phone)

    def click_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    # Вторая страница
    def fill_date(self, date):
        self.send_keys_to_element(OrderPageLocators.DATE_FIELD, date)
        self.click_element(OrderPageLocators.ORDER_BUTTON)  # закрыть календарь

    def select_rental_period(self, period_text):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        options = self.get_elements(OrderPageLocators.RENTAL_OPTIONS)
        for option in options:
            if period_text.lower() in option.text.lower():
                self.click_element_by_element(option)
                break

    def select_color(self, color):
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)

    def click_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    def is_success_message_displayed(self):
        return self.is_element_displayed(OrderPageLocators.SUCCESS_MESSAGE)

    def fill_order_form(self, data):
        self.fill_name(data["name"])
        self.fill_surname(data["surname"])
        self.fill_address(data["address"])
        self.fill_metro(data["metro"])
        self.fill_phone(data["phone"])
        self.click_next()
        self.wait_for_element_visible(OrderPageLocators.DATE_FIELD)
        self.fill_date(data["date"])
        self.select_rental_period(data["rental_period"])
        self.select_color(data["color"])
        self.click_order()
        self.confirm_order()