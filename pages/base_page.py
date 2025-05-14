from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def click(self, locator):
        try:
            self.wait_until_clickable(locator).click()
        except Exception:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, locator, text):
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(text)

    def wait_until_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_element_visible(self, locator):
        try:
            self.wait_until_visible(locator)
            return True
        except TimeoutException:
            return False

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_into_view(self, locator):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def upload_file(self, locator, file_path):
        self.find_element(locator).send_keys(file_path)
