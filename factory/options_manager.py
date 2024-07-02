from selenium import webdriver

import config
from utils.config_parser import get_config


class OptionsManager:

    @staticmethod
    def chrome_options():
        co = webdriver.ChromeOptions()
        co.add_experimental_option('detach', True)
        # if get_config('OPTIONS', 'headless') == 'true':
        if config.headless:
            co.add_argument('--headless')
        # if get_config('OPTIONS', 'incognito') == 'true':
        if config.incognito:
            co.add_argument('--incognito')

        return co
