from utils.element_utils import ElementUtils
from selenium.webdriver.common.by import By


class Footer:
    __footer_sections = By.XPATH, '//footer//h5'
    __footer_links = By.XPATH, './following-sibling::ul//a'

    def __init__(self, driver):
        self.__driver = driver
        self.__util = ElementUtils(self.__driver)

    def get_footer_sections(self):
        return self.__util.get_elements_text(self.__footer_sections)

    def get_footer_links(self):
        footer_sections = self.__util.wait_for_elements_visibility(self.__footer_sections, 10)
        footer_links = []
        for section in footer_sections:
            links = section.find_elements(*self.__footer_links)

            for link in links:
                footer_links.append(link.text)

        return footer_links

    def get_section_links(self, section):
        section_link_xpath = By.XPATH, self.__footer_sections[1] + f"[text()='{section}']/following-sibling::ul//a"
        section_links = self.__util.wait_for_elements_visibility(section_link_xpath, 10)

        links = []
        for link in section_links:
            links.append(link.text)

        return links


