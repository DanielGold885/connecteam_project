from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.job_application_page import JobApplicationPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_all_rnd_positions(driver, applicant_details, cv_file_path):
    home = HomePage(driver)
    home.load()
    home.scroll_to_footer_and_click_careers()

    careers = CareersPage(driver)
    careers.select_rnd_department()

    apply_buttons = careers.get_visible_apply_buttons()
    assert apply_buttons, "No visible Apply buttons found"

    total = len(apply_buttons)
    print(f"🧪 Found {total} visible R&D positions")

    for i in range(total):
        careers.select_rnd_department()
        apply_buttons = careers.get_visible_apply_buttons()
        button = apply_buttons[i]

        print(f"➡️ Clicking R&D job #{i + 1}: {button.get_attribute('href')}")
        driver.execute_script("arguments[0].click();", button)

        try:
            form = JobApplicationPage(driver)
            form.fill_application_form(applicant_details, cv_file_path)
            print(f"✅ Filled form for position #{i + 1}")
        except Exception as e:
            print(f"⚠️ Skipped position #{i + 1}: {str(e)}")

        driver.back()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CareersPage.DEPARTMENT_DROPDOWN)
        )
