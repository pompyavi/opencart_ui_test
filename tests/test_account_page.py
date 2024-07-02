import pytest
from assertpy import assert_that
from constants import account_headers, account_page_title


@pytest.mark.usefixtures('setup_account_page')
class TestAccountPage:

    def test_account_page_title(self):
        page_title = self.account_page.get_page_title()
        assert_that(page_title).is_equal_to(account_page_title)

    def test_account_page_url(self):
        page_url = self.account_page.get_page_url()
        assert_that(page_url).contains('route=account/account')

    def test_logout_link_exists(self):
        assert_that(self.account_page.is_logout_link_exists()).is_true()

    def test_account_headers(self):
        act_account_headers = self.account_page.get_account_headers()
        assert_that(act_account_headers).is_length(4).is_equal_to(account_headers)
