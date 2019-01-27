from abc import ABC, abstractmethod

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from tests_ui.core.locators import *
from tests_ui.core.config import *
from tests_ui.test_data.data import TEST_DATA


class BasePage(ABC):
    def __init__(self, driver):
        self._driver = driver

    def find_element(self, locator_type, locator, timeout=GLOBAL_TIMEOUT):
        return WebDriverWait(self._driver, timeout).until(
            ec.visibility_of_element_located((locator_type, locator)))

    @abstractmethod
    def is_title_matches(self):
        raise NotImplementedError("Implement method")

    @abstractmethod
    def is_url_matches(self):
        raise NotImplementedError("Implement method")


class HomePage(BasePage):
    def is_title_matches(self):
        return self._driver.title == TEST_DATA["home_page_title"]

    def is_url_matches(self, url=None):
        return self._driver.current_url == HOME_PAGE_URL

    def is_login_button_present(self):
        return self.find_element(*HomePageLocators.LOGIN_BUTTON).is_displayed()

    def is_hire_talent_button_present(self):
        return self.find_element(*HomePageLocators.HIRE_TALENT_BUTTON).is_displayed()

    def is_apply_button_present(self):
        return self.find_element(*HomePageLocators.APPLY_BUTTON).is_displayed()

    def navigate_client_page(self):
        careers_button = self.find_element(*HomePageLocators.NAVIGATE_CLIENTS_BUTTON)
        careers_button.click()
        return ClientsPage(self._driver)

    def navigate_enterprise_page(self):
        enterprise_button = self.find_element(*HomePageLocators.NAVIGATE_ENTERPRISE_BUTTON)
        enterprise_button.click()
        return EnterprisePage(self._driver)


class ClientsPage(BasePage):
    def is_title_matches(self):
        return self._driver.title == TEST_DATA["clients_page_title"]

    def is_url_matches(self, url=None):
        return self._driver.current_url == CLIENTS_PAGE_URL


class EnterprisePage(BasePage):
    def is_title_matches(self):
        return self._driver.title == TEST_DATA["enterprise_page_title"]

    def is_url_matches(self, url=None):
        return self._driver.current_url == ENTERPRISE_PAGE_URL
