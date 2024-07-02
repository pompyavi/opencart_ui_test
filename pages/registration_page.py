from selenium.webdriver.common.by import By
from config import register_page_url
from constants import expected_account_created_message
from utils.element_utils import ElementUtils


class RegistrationPage:

    __header = By.TAG_NAME, 'h1'
    __firstname = By.ID, 'input-firstname'
    __lastname = By.ID, 'input-lastname'
    __email = By.ID, 'input-email'
    __telephone = By.ID, 'input-telephone'
    __password = By.ID, 'input-password'
    __confirm_password = By.ID, 'input-confirm'
    __privacy_policy = By.CSS_SELECTOR, "input[type='checkbox']"
    __continue = By.CSS_SELECTOR, "input[type='submit']"
    __account_created_message = By.TAG_NAME, 'h1'
    __logout = By.LINK_TEXT, 'Logout'
    __register = By.LINK_TEXT, 'Register'

    def __init__(self, driver):
        self.__driver = driver
        self.__driver.get(register_page_url)
        self.__util = ElementUtils(self.__driver)

    def get_page_title(self):
        return self.__driver.title

    def get_page_url(self):
        return self.__driver.current_url

    def get_header(self):
        return self.__util.get_element_text(self.__header)

    def register_user(self, firstname, lastname, email, telephone, password, subscribe):
        newsletter = By.XPATH, f"//input[@type='radio' and @name='newsletter' and @value='{subscribe}']"

        self.__util.enter_keys(self.__firstname, firstname)
        self.__util.enter_keys(self.__lastname, lastname)
        self.__util.enter_keys(self.__email, email)
        self.__util.enter_keys(self.__telephone, telephone)
        self.__util.enter_keys(self.__password, password)
        self.__util.enter_keys(self.__confirm_password, password)
        self.__util.click_element(newsletter)
        self.__util.click_element(self.__privacy_policy)
        self.__util.click_element(self.__continue)

        account_created_message = self.__util.wait_for_element_visibility(self.__account_created_message, 10).text

        if account_created_message == expected_account_created_message:
            self.__util.click_element(self.__logout)
            self.__util.wait_for_element_visibility(self.__register, 10).click()
            return True

        else:
            return False




