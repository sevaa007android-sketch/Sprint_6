import allure
import pytest
from data import FAQ_DATA
from pages.main_page import MainPage

class TestFAQ:
    @allure.title("Проверка текста ответа на вопрос №{index}")
    @pytest.mark.parametrize("index, expected_text", FAQ_DATA)
    def test_question_answer(self, driver, index, expected_text):
        main_page = MainPage(driver)
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()
        with allure.step(f"Кликнуть на вопрос {index}"):
            main_page.click_question(index)
        with allure.step("Дождаться появления ответа и проверить текст"):
            main_page.wait_for_answer_visible(index)
            actual_text = main_page.get_answer_text(index)
            assert actual_text == expected_text