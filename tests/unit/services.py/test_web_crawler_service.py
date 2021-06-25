import pytest

from unittest import TestCase
from unittest.mock import patch


from web_crawler.services.web_crawler_service import WebCrawlerService


@pytest.mark.unit_tests
class TestWebCrawlerService(TestCase):

    @patch('web_crawler.services.web_crawler_service.requests.get')
    def test_get_embedded_web(self, mock_get_html):
        # Given
        mock_get_html.return_value.text = """<html><head><title>The Dormouse's story</title></head>
                                                <body>
                                                    <p class="title"><b>The Dormouse's story</b></p>
                                                    <p class="story">Once upon a time there were three little sisters; and their names were
                                                    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                                                    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                                                    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                                                    and they lived at the bottom of a well.</p>
                                                    <p class="story">...</p>
                                          """
        # When
        webs = WebCrawlerService._get_embedded_web('https://google.com')

        # Then
        expected_webs = ['http://example.com/elsie',
                         'http://example.com/lacie',
                         'http://example.com/tillie']

        self.assertEqual(expected_webs, list(webs))

    def test_run_unimplemented(self):
        # Given
        class FakeWebCrawler(WebCrawlerService):
            pass

        # When / Then
        with self.assertRaises(TypeError):
            FakeWebCrawler()
