from selenium import webdriver
from factory.options_manager import OptionsManager


class DriverFactory:

    def __init__(self):
        self.__driver = None

    def init_driver(self, browser: str):

        browser = browser.strip().lower()

        if browser == 'chrome':
            self.__driver = webdriver.Chrome(OptionsManager.chrome_options())

        elif browser == 'firefox':
            self.__driver = webdriver.Firefox()

        else:
            print('Invalid browser....')

        self.__driver.maximize_window()
        self.__driver.delete_all_cookies()

        return self.__driver


