from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from configs.constants import BASE_URL


class HomePage(BasePage):
    URL = BASE_URL

    CAREERS_LINK = (By.LINK_TEXT, "Careers")

    def load(self):
        self.driver.get(self.URL)

    def scroll_to_footer_and_click_careers(self):
        self.scroll_into_view(self.CAREERS_LINK)
        self.click(self.CAREERS_LINK)
