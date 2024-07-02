from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with

import config
from utils.config_parser import get_config
from utils.javascript_utils import JavascriptUtils


class ElementUtils:

    def __init__(self, driver):
        self.__driver = driver
        self.__js = JavascriptUtils(self.__driver)

    def get_element(self, locator):
        element = self.__driver.find_element(*locator)
        # if get_config('OPTIONS', 'flash') == 'true':
        if config.flash:
            self.__js.flash_element(element)
        return element

    def get_elements(self, locator):
        return self.__driver.find_elements(*locator)

    def is_element_displayed(self, locator):
        return self.get_element(locator).is_displayed()

    def click_element(self, locator):
        return self.get_element(locator).click()

    def enter_keys(self, locator, value):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(value)

    def get_element_text(self, locator, timeout=None):
        if timeout:
            element = self.wait_for_element_visibility(locator, timeout)
        else:
            element = self.get_element(locator)
        return element.text

    def get_elements_text(self, locator, timeout=None):
        if timeout:
            elements = self.wait_for_elements_visibility(locator, timeout)
        else:
            elements = self.get_elements(locator)
        return [element.text for element in elements]

    # **************Wait Utils***************************************

    def wait_for_element_visibility(self, locator, timeout):
        wait = WebDriverWait(self.__driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_elements_visibility(self, locator, timeout):
        wait = WebDriverWait(self.__driver, timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    # ********************Relative locator utils************************

    def get_below_elements(self, locator, element):
        return self.__driver.find_elements(locate_with(*locator).below(element))

    # ****************Select Dropdown utils******************************

    def select_option_by_visible_text(self, locator, value, timeout):
        element = self.wait_for_element_visibility(locator, timeout)
        select = Select(element)
        select.select_by_visible_text(value)
