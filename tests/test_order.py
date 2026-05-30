import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

# Данные для параметризации:
ORDER_DATA = [
    ("top", {
        "name": "Иван",
        "surname": "Иванов",
        "address": "ул. Пушкина, 10",
        "metro": "Сокольники",
        "phone": "+79998887766",
        "date": "30.06.2026",
        "rental_period": "сутки",
        "color": "black"
    }),
    ("bottom", {
        "name": "Петр",
        "surname": "Петров",
        "address": "пр. Ленина, 5",
        "metro": "Лубянка",
        "phone": "+79123456789",
        "date": "31.05.2025",
        "rental_period": "двое суток",
        "color": "grey"
    })
]

class TestOrder:
    @allure.title("Оформление заказа самоката через кнопку {button_type}")
    @pytest.mark.parametrize("button_type, order_data", ORDER_DATA)
    def test_order_scooter(self, driver, button_type, order_data):
        # Открыть главную страницу
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Закрыть баннер куки, если он мешает (особенно для нижней кнопки)
        main_page.close_cookie_banner()

        # Нажать на соответствующую кнопку «Заказать»
        if button_type == "top":
            main_page.click_order_top_button()
        else:
            main_page.click_order_bottom_button()

        # Заполнить форму заказа (универсальный метод)
        order_page.fill_order_form(order_data)

        # Проверить, что появилось сообщение об успешном заказе
        success_text = order_page.get_success_message()
        assert "Заказ оформлен" in success_text