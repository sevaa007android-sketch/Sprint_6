import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import DEFAULT_TIMEOUT
from pages.main_page import MainPage

class TestLogos:
    @allure.title("Переход на главную по логотипу Самокат с другой страницы")
    def test_scooter_logo_redirects_to_main(self, driver):
        # Открыть страницу заказа (не главную)
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page = MainPage(driver)
        # Кликнуть по логотипу Самокат
        main_page.click_scooter_logo()
        # Проверить, что URL стал главной страницей (используем глобальный таймаут)
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Открытие Дзена по логотипу Яндекса в новом окне")
    def test_yandex_logo_opens_dzen(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPage(driver)
        # Клик по логотипу Яндекса и переключение на новое окно
        main_page.click_yandex_logo()
        main_page.switch_to_new_window() 
        # Проверить, что URL содержит dzen.ru
        WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url