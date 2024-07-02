import pytest

import config
from factory.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.search_result_page import SearchResultPage


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup_teardown(request):
    browser_name = request.config.getoption("browser_name")
    driver = DriverFactory().init_driver(browser_name)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
def setup_login_page(request, setup_teardown):
    request.cls.login_page = LoginPage(request.cls.driver)


@pytest.fixture(scope='class')
def setup_account_page(request, setup_login_page):
    request.cls.account_page = request.cls.login_page.do_login()


@pytest.fixture(scope='class')
def setup_search_result_page(request, setup_teardown):
    request.cls.driver.get(config.home_page_url)
    request.cls.search_results_page = SearchResultPage(request.cls.driver)


@pytest.fixture(scope='class')
def setup_registration_page(request, setup_teardown):
    request.cls.registration_page = RegistrationPage(request.cls.driver)


def pytest_runtest_setup(item):
    print(f"Setting up test: {item.name}")
    print(f"Module: {item.module.__name__}")
    if item.cls:
        print(f"Class: {item.cls.__name__}")


def pytest_runtest_teardown(item, nextitem):
    print(f"Tearing down test: {item.name}")
    print(f"Tearing down test: {nextitem.name}")


def pytest_runtest_logreport(report):
    if report.when == 'call':
        test_name = report.nodeid
        module_name = report.location[0]
        print(report.location)
        test_result = 'PASSED' if report.passed else 'FAILED' if report.failed else 'SKIPPED'

        print(f"Test name: {test_name}")
        print(f"Module name: {module_name}")
        if report.location[2]:
            class_name = report.location[2].split(".")[0] if "." in report.location[2] else None
            if class_name:
                print(f"Class name: {class_name}")
        print(f"Test result: {test_result}")

