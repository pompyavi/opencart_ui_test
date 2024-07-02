from pages.common.footer_component import Footer
from utils.element_utils import ElementUtils
from selenium.webdriver.common.by import By


class AccountPage(Footer):
    __account_header = By.CSS_SELECTOR, '#content h2'
    __logout_link = By.LINK_TEXT, 'Logout'

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        self.__util = ElementUtils(self.__driver)

    def get_page_title(self):
        return self.__driver.title

    def get_page_url(self):
        return self.__driver.current_url

    def get_account_headers(self):
        return self.__util.get_elements_text(self.__account_header)

    def is_logout_link_exists(self):
        return self.__util.is_element_displayed(self.__logout_link)
