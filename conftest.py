import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

BASE_URL = "https://qa-scooter.praktikum-services.ru/"
ORDER_ENDPOINT = "order"
DEFAULT_TIMEOUT = 7

@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()