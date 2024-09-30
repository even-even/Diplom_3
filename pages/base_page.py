from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seletools.actions import drag_and_drop
from data import Timeouts

class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open_url(self, url_page=""):
        self.driver.get(f"{self.base_url}/{url_page}")

    def drag_and_drop(self, source, target):
        drag_and_drop(self.driver, source, target)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, timeout=Timeouts.LARGE):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.visibility_of_element(locator).click()

    def enter_text(self, locator, text, timeout=Timeouts.MEDIUM):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def visibility_of_element(self, locator, timeout=Timeouts.MEDIUM):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
