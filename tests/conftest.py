import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.passport_2 import PassportPage2

logger = logging.getLogger("qa")

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://berpress.github.io/ui-passport-demo/",
                     help="url")

# @pytest.fixture(scope="session")
# def passport_page(request):
#     url = request.config.getoption('--url')
#     chrome_options = Options()
#     chrome_options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome()
#     driver.get(url)
#     passport_page = PassportPage(driver)
#     yield passport_page
#     driver.quit()

@pytest.fixture(scope="session")
def passport_page_2(request):
    url = request.config.getoption('--url')
    logger.info(f'Start app on url {url}')
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome()
    driver.get(url)
    passport_page = PassportPage2(driver)
    yield passport_page
    logger.info(f'Stop tests')
    driver.quit()