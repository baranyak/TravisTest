from selenium.webdriver.common.by import By


class HomePageLocators:
    NAVIGATE_CLIENTS_BUTTON = (By.XPATH, "//a[text()='Clients' and @class='page_header_menu-link']")
    NAVIGATE_ENTERPRISE_BUTTON = (By.XPATH, "//a[text()='Enterprise' and @class='page_header_menu-link']")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class, 'button') and text()='Log in']")
    HIRE_TALENT_BUTTON = (By.XPATH, "//a[contains(@class, 'button') and text()='Hire Top Talent']")
    APPLY_BUTTON = (By.XPATH, "//a[contains(@class, 'button') and text()='Apply as a Freelancer']")
