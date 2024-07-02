from selenium.webdriver.common.by import By
from pages.account_page import AccountPage
from pages.common.footer_component import Footer
from utils.element_utils import ElementUtils
from config import login_page_url
from utils.config_parser import get_config


class LoginPage(Footer):
    __email_field = By.ID, 'input-email'
    __password_field = By.ID, 'input-password'
    __login_button = By.CSS_SELECTOR, 'input[value="Login"]'
    __forgot_password_link = By.LINK_TEXT, 'Forgotten Password'
    __right_column_links = By.CSS_SELECTOR, '#column-right a'

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        # self.__driver.get(login_page_url)
        self.__driver.get(get_config('WEBSITE', 'login_page_url'))
        self.__util = ElementUtils(self.__driver)

    def get_page_title(self):
        return self.__driver.title

    def get_page_url(self):
        return self.__driver.current_url

    def is_forgot_pass_link_exists(self):
        return self.__util.is_element_displayed(self.__forgot_password_link)

    def get_right_column_links(self):
        return self.__util.get_elements_text(self.__right_column_links)

    def do_login(self):
        self.__util.wait_for_element_visibility(self.__email_field, 5).send_keys('pompyavi@gmail.com')
        self.__util.enter_keys(self.__password_field, 'Killbill11@')
        self.__util.click_element(self.__login_button)
        return AccountPage(self.__driver)
