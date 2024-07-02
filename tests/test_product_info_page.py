import pytest
from assertpy import assert_that
from constants import macbook_pro_metadata, added_to_cart_message


@pytest.mark.usefixtures('setup_search_result_page')
class TestProductInfoPage:

    @pytest.mark.parametrize('search_key, product', [('Macbook', 'MacBook Air')])
    def test_product_header(self, search_key, product):
        self.search_results_page.search_product(search_key)
        product_info_page = self.search_results_page.select_product(product)
        assert_that(product_info_page.get_product_header()).is_equal_to(product)

    @pytest.mark.parametrize('search_key, product, expected_count', [('Macbook', 'MacBook Air', 4)])
    def test_product_images_count(self, search_key, product, expected_count):
        self.search_results_page.search_product(search_key)
        product_info_page = self.search_results_page.select_product(product)
        assert_that(product_info_page.get_product_images_count()).is_equal_to(expected_count)

    @pytest.mark.parametrize('search_key, product, expected_count', [('Macbook', 'MacBook Air', 4)])
    def test_product_images_count(self, search_key, product, expected_count):
        self.search_results_page.search_product(search_key)
        product_info_page = self.search_results_page.select_product(product)
        assert_that(product_info_page.get_product_description()).is_not_empty()

    def test_product_metadata(self):
        self.search_results_page.search_product('Macbook')
        product_info_page = self.search_results_page.select_product('MacBook Pro')
        assert_that(product_info_page.get_product_info()).is_equal_to(macbook_pro_metadata)

    def test_add_to_cart(self):
        self.search_results_page.search_product('Macbook')
        product_info_page = self.search_results_page.select_product('MacBook Pro')
        assert_that(product_info_page.add_product_to_cart()).is_equal_to(added_to_cart_message)




