import pytest

from unittest import TestCase
from unittest.mock import patch


from web_crawler.web_crawler import WebCrawler


@pytest.mark.unit_tests
class TestWebCrawler(TestCase):

    @patch('web_crawler.web_crawler.requests')
    def test_web_crawler(self, mock_requests):
        # Given
        mock_requests.get.return_value.text = '<html><body><a href="http://patriciotula.com/neighbor"></a></body></html>'
        web_crawler = WebCrawler('http://patriciotula.com')

        # When
        webs = web_crawler.crawl_the_web()

        # Then
        self.assertEqual(webs, ['http://patriciotula.com/neighbor'])

