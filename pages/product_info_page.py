from selenium.webdriver.common.by import By

from utils.element_utils import ElementUtils


class ProductInfoPage:
    __product_header = By.TAG_NAME, 'h1'
    __product_images = By.CSS_SELECTOR, '.thumbnails a'
    __product_description = By.CSS_SELECTOR, '#tab-description>div'
    __product_metadata = By.CSS_SELECTOR, '#content ul.list-unstyled:first-of-type>li'
    __product_price_data = By.CSS_SELECTOR, '#content ul.list-unstyled:last-of-type>li'
    __added_to_cart_message = By.CLASS_NAME, 'alert-success'
    __add_to_cart_button = By.ID, 'button-cart'

    def __init__(self, driver):
        self.__driver = driver
        self.__util = ElementUtils(self.__driver)

    def get_product_header(self):
        return self.__util.get_element_text(self.__product_header, 10)

    def get_product_images_count(self):
        return len(self.__util.wait_for_elements_visibility(self.__product_images, 10))

    def get_product_description(self):
        return self.__util.get_element_text(self.__product_description)

    def get_product_info(self):
        product_info = {'product_name': self.get_product_header()}
        self.__get_product_metadata(product_info)
        self.__get_product_price_data(product_info)
        return product_info

    def __get_product_metadata(self, product_info):
        product_meta_data_list = self.__util.get_elements_text(self.__product_metadata, 10)
        for product_metadata in product_meta_data_list:
            metadata = product_metadata.split(':')
            key = metadata[0].strip()
            value = metadata[1].strip()
            product_info.update({key: value})

    def __get_product_price_data(self, product_info):
        product_price_data_list = self.__util.get_elements_text(self.__product_price_data, 10)
        product_price = product_price_data_list[0].strip()
        ex_tax = product_price_data_list[1].split(':')[1].strip()
        product_info.update({'product_price': product_price})
        product_info.update({'ex_tax': ex_tax})

    def add_product_to_cart(self):
        self.__util.click_element(self.__add_to_cart_button)
        message = self.__util.get_element_text(self.__added_to_cart_message, 10)
        return message[:-2]
