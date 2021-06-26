import pytest

from unittest import TestCase
from unittest.mock import patch

from web_crawler import WebCrawler


@pytest.mark.unit_tests
@patch('web_crawler.WebCrawler._get_embedded_web')
class TestWebCrawler(TestCase):

    def test_run_single_node_tree(self, mock_get_webs):
        """
        Single node tree test.
        Expected:
        mock.com
        """
        # Given
        mock_get_webs.return_value = []
        web_crawler = WebCrawler('mock.com')
        
        # When
        websites = web_crawler.run()

        # Then
        expected_websites = 'mock.com\n\tmock.com/1\n\tmock.com/2\n\tmock.com/3'

        self.assertEqual(expected_websites, websites)

    def test_run_simple_tree(self, mock_get_webs):
        """
        Simple Tree test.
        Expected:
        mock.com
            mock.com/1
            mock.com/2
            mock.com/3
        """
        # Given
        mock_get_webs.return_value = ['mock.com/1', 'mock.com/2', 'mock.com/3']
        web_crawler = WebCrawler('mock.com')
        
        # When
        websites = web_crawler.run()

        # Then
        expected_websites = 'mock.com\n\tmock.com/1\n\tmock.com/2\n\tmock.com/3'

        self.assertEqual(expected_websites, websites)

    def test_run_circular_graph(self, mock_get_webs):
        """
        Graph with circular dependency.
        Expected:
        mock.com
            mock.com/1
                mock.com
            mock.com/2
            mock.com/3
        """
        # Given
        mock_get_webs.side_effect = [['mock.com/1', 'mock.com/2', 'mock.com/3'], ['mock.com']]
        web_crawler = WebCrawler('mock.com')
        
        # When
        websites = web_crawler.run()

        # Then
        expected_websites = 'mock.com\n\tmock.com/1\n\t\tmock.com\n\tmock.com/2\n\tmock.com/3'

        self.assertEqual(expected_websites, websites)
