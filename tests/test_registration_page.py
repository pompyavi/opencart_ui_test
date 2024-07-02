import pytest
import constants
from assertpy import assert_that
from utils.common_utils import get_random_gmail
from utils.excel_util import get_test_data


@pytest.mark.usefixtures('setup_registration_page')
class TestLoginPage:

    @pytest.mark.parametrize('firstname, lastname, telephone, password, subscribe',
                             get_test_data(constants.register_sheet))
    def test_user_registration(self, firstname, lastname, telephone, password, subscribe):
        assert_that(self.registration_page.register_user(firstname, lastname,
                                                         get_random_gmail(), telephone, password, subscribe)).is_true()
