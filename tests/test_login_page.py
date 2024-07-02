import pytest
from constants import right_column_links, login_page_title, footer_sections, footer_links
from config import login_page_url
from assertpy import assert_that


@pytest.mark.usefixtures('setup_login_page')
class TestLoginPage:

    def test_login_page_title(self):
        assert_that(self.login_page.get_page_title()).is_equal_to(login_page_title)

    def test_login_page_url(self):
        assert_that(self.login_page.get_page_url()).is_equal_to(login_page_url)

    def test_forgot_password_link_exists(self):
        assert_that(self.login_page.is_forgot_pass_link_exists()).is_true()

    def test_right_column_links(self):
        right_col_links = self.login_page.get_right_column_links()
        assert_that(right_col_links).is_length(13).is_equal_to(right_column_links)

    def test_footer_sections_exist(self):
        act_footer_sections = self.login_page.get_footer_sections()
        assert_that(act_footer_sections).is_length(4).is_equal_to(footer_sections)

    def test_footer_links(self):
        act_footer_links = self.login_page.get_footer_links()
        assert_that(act_footer_links).is_length(15).is_equal_to(footer_links)

    def test_information_section_of_footer(self):
        act_info_links = self.login_page.get_section_links('Information')
        assert_that(act_info_links).is_length(4)

    def test_login(self):
        account_page = self.login_page.do_login()
        assert_that(account_page.is_logout_link_exists()).is_true()
