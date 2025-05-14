from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CareersPage(BasePage):
    DEPARTMENT_DROPDOWN = (By.ID, "department-filter")
    APPLY_NOW_BUTTONS = (By.XPATH, "//a[text()='Apply now' and not(ancestor::*[contains(@style,'display: none')])]")

    def select_rnd_department(self):
        dropdown = self.find_element(self.DEPARTMENT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text("R&D")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.APPLY_NOW_BUTTONS)
        )

    def get_visible_apply_buttons(self):
        all_buttons = self.find_elements(self.APPLY_NOW_BUTTONS)
        return [b for b in all_buttons if b.is_displayed()]
