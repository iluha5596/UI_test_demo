import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope='function')
def driver():
    options = ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
        except KeyError:
            return
        screenshot_path = f"screenshots/screenshot_{item.name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved as {screenshot_path}")
