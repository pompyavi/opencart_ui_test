import pytest
from assertpy import assert_that


@pytest.mark.usefixtures('setup_search_result_page')
class TestSearchResultPage:

    @pytest.mark.parametrize('product', ['Macbook', 'iMac', 'Samsung', 'Sony', 'Aivi'])
    def test_product_search_count(self, product):
        self.search_results_page.search_product(product)
        assert_that(self.search_results_page.get_search_results_count()).is_greater_than(0)

    @pytest.mark.parametrize('product', ['Macbook', 'iMac', 'Samsung', 'Sony', 'Aivi'])
    def test_result_is_sorted(self, product):
        self.search_results_page.search_product(product)
        self.search_results_page.sort_results_by_name('Name (Z - A)')
        results = self.search_results_page.get_search_results()
        assert_that(results).is_sorted(reverse=True)



