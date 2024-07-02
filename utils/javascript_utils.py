import time


class JavascriptUtils:

    def __init__(self, driver):
        self.__driver = driver

    def change_color(self, rgb_color, element):
        self.__driver.execute_script(f"arguments[0].style.backgroundColor='{rgb_color}'", element)
        try:
            time.sleep(0.02)
        except InterruptedError:
            pass

    def flash_element(self, element):
        current_color = element.value_of_css_property('background-color')
        for _ in range(10):
            self.change_color('rgb(0,200,0)', element)
            self.change_color(current_color, element)

