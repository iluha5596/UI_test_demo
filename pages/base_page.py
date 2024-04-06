from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, how, what):
        return self.driver.find_element(how, what)

    def find_elements(self, how, what):
        return self.driver.find_elements(how, what)

    def visibility_of_element_locator(self, how, what, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))

    def element_is_clickable(self, how, what, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable((how, what)))
