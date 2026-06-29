import allure
from conftest import BASE_URL
from pages.main_page import MainPage

class TestLogos:
    @allure.title("Переход на главную по логотипу Самокат с другой страницы")
    def test_scooter_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть страницу заказа (не главную)"):
            main_page.open_order_page()
        with allure.step("Кликнуть по логотипу Самокат"):
            main_page.click_scooter_logo()
        with allure.step("Проверить, что URL стал главной страницей"):
            assert main_page.is_current_url_equal(BASE_URL), "Не удалось перейти на главную страницу"

    @allure.title("Открытие Дзена по логотипу Яндекса в новом окне")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        with allure.step("Кликнуть по логотипу Яндекса"):
            main_page.click_yandex_logo()
        with allure.step("Переключиться на новое окно"):
            main_page.switch_to_new_window()
        with allure.step("Проверить, что URL содержит 'dzen.ru'"):
            assert main_page.is_url_contains("dzen.ru"), "Не удалось открыть Дзен"