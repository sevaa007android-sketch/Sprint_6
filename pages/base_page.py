from conftest import DEFAULT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def send_keys_to_element(self, locator, text):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def clear_and_send_keys(self, locator, text):
        element = WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        ).text

    def get_elements(self, locator):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_element_by_element(self, element):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.element_to_be_clickable(element))
        element.click()

    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_url(self, url):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.url_to_be(url))

    def wait_for_url_contains(self, text):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(lambda d: text in d.current_url)

    def wait_for_new_window(self):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(lambda d: len(d.window_handles) > 1)

    def switch_to_new_window(self):
        self.wait_for_new_window()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def open_url(self, url):
        self.driver.get(url)