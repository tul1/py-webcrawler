import pytest

from unittest import TestCase
from unittest.mock import patch, MagicMock, call


from web_crawler.services.web_crawler_service import WebCrawlerService


class FakeCrawler(WebCrawlerService):
    def __init__(self, url):
        super().__init__(url)

    def run(self):
        pass


@pytest.mark.unit_tests
class TestWebCrawlerService(TestCase):

    @patch('web_crawler.services.web_crawler_service.BeautifulSoup')
    @patch('web_crawler.services.web_crawler_service.requests.get')
    @patch('web_crawler.services.web_crawler_service.WebCrawlerService._format_url')
    def test_get_embedded_webs(self, mock_format_url, mock_get_html, mock_beautifulsoup):
        # Given
        fake_crawler = FakeCrawler('http://example.com/')
        mock_beautifulsoup.return_value.find_all.return_value = [1, 2, 3, 4, 5, 6, 7]
        mock_format_url.side_effect = [None, 'http://example.com/elsie',
                                       None, 'http://example.com/lacie',
                                       None, 'http://example.com/tillie',
                                       None]

        # When
        webs = fake_crawler.get_embedded_webs('http://example.com/')

        # Then
        expected_webs = ['http://example.com/elsie',
                         'http://example.com/lacie',
                         'http://example.com/tillie']

        self.assertEqual(expected_webs, list(webs))
        mock_get_html.assert_called_once_with('http://example.com/')
        mock_beautifulsoup.assert_called_once_with(mock_get_html.return_value.text, features='html5lib')
        mock_beautifulsoup.return_value.find_all.assert_called_with('a')
        calls = [call(1), call(2), call(3), call(4), call(5), call(6), call(7)]
        mock_format_url.assert_has_calls(calls)

    def test_format_url(self):
        """ Test format url """
        # Given
        fake_crawler = FakeCrawler('http://example.com/')

        # When / Then
        self.assertEqual('http://example.com/elsie',
                         fake_crawler._format_url(MagicMock(**{'get.return_value': 'http://example.com/elsie'})))
        self.assertIsNone(fake_crawler._format_url(MagicMock(**{'get.return_value': '/elsie'})))
        self.assertIsNone(fake_crawler._format_url(MagicMock(**{'get.return_value': 'elsie'})))
        self.assertIsNone(fake_crawler._format_url(MagicMock(**{'get.return_value': None})))

        self.assertEqual('http://example.com/lacie',
                         fake_crawler._format_url(MagicMock(**{'get.return_value': 'http://example.com/lacie'})))
        self.assertEqual('http://example.com/tillie',
                         fake_crawler._format_url(MagicMock(**{'get.return_value': '/tillie'})))

    @patch('web_crawler.services.web_crawler_service.requests.get')
    def test_get_embedded_webs_requests_raises(self, mock_get_html):
        # Given
        fake_crawler = FakeCrawler('http://example.com/')
        mock_get_html.side_effect = Exception('Boom!')

        # When
        webs = fake_crawler.get_embedded_webs('https://mock.com')

        # Then
        self.assertEqual([], list(webs))

    @patch('web_crawler.services.web_crawler_service.BeautifulSoup')
    def test_get_embedded_webs_beautifulsoup_raises(self, mock_beautifulsoup):
        # Given
        fake_crawler = FakeCrawler('http://example.com/')
        mock_beautifulsoup.side_effect = Exception('Boom!')

        # When
        webs = fake_crawler.get_embedded_webs('https://mock.com')

        # Then
        self.assertEqual([], list(webs))

    def test_run_unimplemented(self):
        with self.assertRaises(NotImplementedError):
            fake_crawler = WebCrawlerService.run(MagicMock())
