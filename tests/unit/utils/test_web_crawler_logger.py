import pytest

from unittest import TestCase
from unittest.mock import patch

from web_crawler.utils.singleton import Singleton
from web_crawler.utils.web_crawler_logger import WebCrawlerLogger


@pytest.mark.unit_tests
@patch('web_crawler.utils.web_crawler_logger.logging')
class TestWebCrawlerLogger(TestCase):

    def setUp(self):
        try:
            Singleton._instances.pop(WebCrawlerLogger)
        except KeyError:
            pass
    
    def test_init(self, logging_mock):
        # When
        first = WebCrawlerLogger()
        second =  WebCrawlerLogger()

        # Then
        assert first is second
        logging_mock.getLogger.assert_called_once_with('web-crawler')
        logging_mock.getLogger.return_value.setLevel.assert_called_once_with(logging_mock.DEBUG)
        # test console handler added
        logging_mock.StreamHandler.assert_called_once_with()
        logging_mock.StreamHandler.return_value.setLevel.assert_called_once_with(logging_mock.DEBUG)
        logging_mock.StreamHandler.return_value.setFormatter.assert_called_once_with(logging_mock.Formatter.return_value)
        logging_mock.getLogger.return_value.addHandler.assert_called_once_with(logging_mock.StreamHandler.return_value)

    def test_logger_returned(self, logging_mock):
        assert logging_mock.getLogger.return_value == WebCrawlerLogger().get_logger()
