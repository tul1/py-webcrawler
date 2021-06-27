import pytest

from unittest import TestCase
from unittest.mock import patch, MagicMock


from web_crawler.services.web_crawler_service import WebCrawlerService


@pytest.mark.unit_tests
class TestWebCrawlerService(TestCase):

    @patch('web_crawler.services.web_crawler_service.BeautifulSoup')
    @patch('web_crawler.services.web_crawler_service.requests.get')
    def test_get_embedded_web(self, mock_get_html, mock_beautifulsoup):
        # Given
        mock_beautifulsoup.return_value.find_all.return_value = [MagicMock(**{'get.return_value': 'http://example.com/elsie'}),
                                                                 MagicMock(**{'get.return_value': 'http://example.com/lacie'}),
                                                                 MagicMock(**{'get.return_value': 'http://example.com/tillie'})]

        # When
        webs = WebCrawlerService._get_embedded_web('https://mock.com')

        # Then
        expected_webs = ['http://example.com/elsie',
                         'http://example.com/lacie',
                         'http://example.com/tillie']

        self.assertEqual(expected_webs, list(webs))
        mock_get_html.assert_called_once_with('https://mock.com')
        mock_beautifulsoup.assert_called_once_with(mock_get_html.return_value.text, features='html5lib')
        mock_beautifulsoup.return_value.find_all.assert_called_with('a')


    def test_run_unimplemented(self):
        # Given
        class FakeWebCrawler(WebCrawlerService):
            pass

        # When / Then
        with self.assertRaises(TypeError):
            FakeWebCrawler()

    @patch('web_crawler.services.web_crawler_service.requests.get')
    def test_get_embedded_web_requests_raises(self, mock_get_html):
        # Given
        mock_get_html.side_effect = Exception('Boom!')

        # When
        webs = WebCrawlerService._get_embedded_web('https://mock.com')

        # Then
        self.assertEqual([], list(webs))

    @patch('web_crawler.services.web_crawler_service.BeautifulSoup')
    def test_get_embedded_web_beautifulsoup_raises(self, mock_beautifulsoup):
        # Given
        mock_beautifulsoup.side_effect = Exception('Boom!')

        # When
        webs = WebCrawlerService._get_embedded_web('https://mock.com')

        # Then
        self.assertEqual([], list(webs))
