import pytest

from unittest import TestCase
from unittest.mock import patch

from web_crawler.utils.exceptions import WebCrawlerException


class TestWebCrawlerException(TestCase):

    @patch('web_crawler.utils.exceptions.WebCrawlerLogger')
    def test_init(self, mock_logger):
        # When
        WebCrawlerException('error_message')

        # Then
        mock_logger.return_value.get_logger.return_value.error.assert_called_once_with('error_message')
