import os
import sys

sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__) + '/../')

import tests_ui.core.pages as pages
from tests_ui.tests.base_test import BaseTest



class TestHomePage(BaseTest):
    def test_elements_presence(self):
        main_page = pages.HomePage(self.driver)

        assert main_page.is_url_matches()
        assert main_page.is_title_matches()
        assert main_page.is_login_button_present()
        assert main_page.is_hire_talent_button_present()
        assert main_page.is_apply_button_present()

    def test_navigate_to_clients_page(self):
        clients_page = pages.HomePage(self.driver).navigate_client_page()

        assert clients_page.is_url_matches()
        assert clients_page.is_title_matches()

    def test_navigate_to_enterprise_page(self):
        enterprise_page = pages.HomePage(self.driver).navigate_enterprise_page()

        assert enterprise_page.is_url_matches()
        assert enterprise_page.is_title_matches()
