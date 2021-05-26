import pytest

from unittest import TestCase
from unittest.mock import patch, MagicMock


from web_crawler.web_crawler import WebCrawler


@pytest.mark.unit_tests
@patch('web_crawler.web_crawler.requests.get')
class TestWebCrawler(TestCase):

    def test_web_crawler_single_neighbor(self, mock_get_sites):
        # Given
        mock_get_sites.return_value.text = '<html><body><a href="http://patriciotula.com/neighbor"></a></body></html>'
        web_crawler = WebCrawler('http://patriciotula.com')

        # When
        webs = web_crawler.crawl_the_web()

        # Then
        self.assertEqual(webs, ['http://patriciotula.com/neighbor'])


    def test_web_crawler_multiple_neighbors(self, mock_get_sites):
        # Given
        original_site = '<html><body><a href="http://patriciotula.com/neighbor1"></a></body></html>'
        first_neighbor_site = '<html><body><a href="http://patriciotula.com/neighbor2"></a></body></html>'
        second_neighbor_site = '<html><body><a href="http://patriciotula.com"></a></body></html>'
        mock_get_sites.side_effect = [MagicMock(text=original_site),
                                      MagicMock(text=first_neighbor_site),
                                      MagicMock(text=second_neighbor_site)]
        web_crawler = WebCrawler('http://patriciotula.com')

        # When
        webs = web_crawler.crawl_the_web()

        # Then
        self.assertEqual(webs, ['http://patriciotula.com/neighbor1', 'http://patriciotula.com/neighbor2'])