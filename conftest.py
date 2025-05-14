import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
import os


@pytest.fixture(autouse=True)
def chrome_web_driver_base(request):
    chrome_web_driver: WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--disable-notifications")  # optional but helpful

    try:
        service = Service()
        chrome_web_driver = webdriver.Chrome(
            service=service, options=options
        )
    except Exception:
        downloaded_binary_path = ChromeDriverManager().install()
        service = Service(executable_path=downloaded_binary_path)
        chrome_web_driver = webdriver.Chrome(
            service=service, options=options
        )

    chrome_web_driver.maximize_window()
    yield chrome_web_driver
    chrome_web_driver.quit()  # safer than .close()


@pytest.fixture
def driver(chrome_web_driver_base):
    return chrome_web_driver_base


@pytest.fixture(scope="session")
def applicant_details():
    return {
        "first_name": "Daniel",
        "last_name": "Gold",
        "email": "daniel.gold@example.com",
        "phone": "+972541234567"
    }

@pytest.fixture(scope="session")
def cv_file_path():
    return str(Path(__file__).parent / "example_cv.pdf")

@pytest.fixture
def applicant_details():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890"
    }

@pytest.fixture
def cv_file_path():
    return os.path.abspath("assets/example_cv.pdf")
