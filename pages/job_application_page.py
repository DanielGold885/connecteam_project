from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class JobApplicationPage(BasePage):
    IFRAME = (By.ID, "grnhse_iframe")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    CV_UPLOAD = (By.CSS_SELECTOR, "input[type='file']")
    CLOSED_ALERT = (By.XPATH, "//*[contains(text(), 'no longer open')]")

    def is_position_closed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.CLOSED_ALERT)
            )
            return True
        except TimeoutException:
            return False

    def switch_to_form_iframe(self):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(self.IFRAME)
        )

    def fill_application_form(self, details, cv_path):
        self.switch_to_form_iframe()

        if self.is_position_closed():
            print("⚠️ Job is closed — skipping.")
            self.driver.switch_to.default_content()
            return False

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        self.find_element(self.FIRST_NAME).send_keys(details["first_name"])
        self.find_element(self.LAST_NAME).send_keys(details["last_name"])
        self.find_element(self.EMAIL).send_keys(details["email"])
        self.find_element(self.PHONE).send_keys(details["phone"])
        self.find_element(self.CV_UPLOAD).send_keys(cv_path)

        self.driver.switch_to.default_content()
        return True
