import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope='function')
def driver():
    options = ChromeOptions()
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    yield driver
    driver.quit()
