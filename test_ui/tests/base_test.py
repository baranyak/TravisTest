import sys

from selenium import webdriver

from tests_ui.core.config import HOME_PAGE_URL


class BaseTest:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(HOME_PAGE_URL)

    def teardown_method(self, method):
        if sys.exc_info()[0]:
            self.driver.save_screenshot("results/{0}.png".format(method.__name__))
        self.driver.quit()
