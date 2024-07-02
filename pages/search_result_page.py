from selenium.webdriver.common.by import By
from pages.common.search_component import Search
from pages.product_info_page import ProductInfoPage
from utils.element_utils import ElementUtils


class SearchResultPage(Search):

    __search_results = By.CSS_SELECTOR, '.row .caption a'
    __sort_by_dropdown = By.ID, 'input-sort'

    def __init__(self, driver):
        self.__driver = driver
        self.__util = ElementUtils(self.__driver)

    def search_product(self, product):
        self.__util.enter_keys(Search.search_field, product)
        self.__util.click_element(self.search_icon)
        return SearchResultPage(self.__driver)

    def get_search_results_count(self):
        return len(self.__util.wait_for_elements_visibility(self.__search_results, 10))

    def sort_results_by_name(self, order):
        self.__util.select_option_by_visible_text(self.__sort_by_dropdown, order, 10)

    def get_search_results(self):
        return self.__util.get_elements_text(self.__search_results, 10)

    def select_product(self, product):
        product = By.LINK_TEXT, product
        self.__util.wait_for_element_visibility(product, 10).click()
        return ProductInfoPage(self.__driver)



