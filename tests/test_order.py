import allure
from data import ORDER_DATA_TOP, ORDER_DATA_BOTTOM
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:
    @allure.title("Оформление заказа самоката через верхнюю кнопку «Заказать»")
    def test_order_scooter_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Закрыть баннер куки, если мешает"):
            main_page.close_cookie_banner()

        with allure.step("Нажать верхнюю кнопку «Заказать»"):
            main_page.click_order_top_button()

        with allure.step("Заполнить форму заказа и подтвердить"):
            order_page.fill_order_form(ORDER_DATA_TOP)

        with allure.step("Проверить, что появилось сообщение об успехе"):
            success_text = order_page.get_success_message()
            assert "Заказ оформлен" in success_text

    @allure.title("Оформление заказа самоката через нижнюю кнопку «Заказать»")
    def test_order_scooter_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Закрыть баннер куки, если мешает"):
            main_page.close_cookie_banner()

        with allure.step("Нажать нижнюю кнопку «Заказать»"):
            main_page.click_order_bottom_button()

        with allure.step("Заполнить форму заказа и подтвердить"):
            order_page.fill_order_form(ORDER_DATA_BOTTOM)

        with allure.step("Проверить, что появилось сообщение об успехе"):
            success_text = order_page.get_success_message()
            assert "Заказ оформлен" in success_text