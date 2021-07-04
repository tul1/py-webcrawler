import pytest

from unittest import TestCase
from unittest.mock import patch, MagicMock

from web_crawler.web_crawler import WebCrawler
from web_crawler.models.web_node import WebNode


@pytest.mark.unit_tests
@patch('web_crawler.WebCrawler.get_embedded_webs')
class TestWebCrawler(TestCase):

    def test_run_single_node(self, mock_get_webs):
        """
        Single node test.
        """
        # Given
        mock_get_webs.return_value = []
        web_crawler = WebCrawler(url_root_web='mock.com')

        # When
        web_crawler.run()

        # Then
        expected_web_node = WebNode(url='mock.com')

        self.assertEqual(expected_web_node, web_crawler.root_web)

    def test_run_simple_tree(self, mock_get_webs):
        """
        Simple Tree test. Three looks like this:
                        mock.com/1
                    /
            mock.com -  mock.com/2
                    \
                        mock.com/3
        """
        # Given
        mock_get_webs.side_effect = [['mock.com/1', 'mock.com/2', 'mock.com/3'], [], [], []]
        web_crawler = WebCrawler(url_root_web='mock.com')

        # When
        web_crawler.run()

        # Then
        expected_web_tree = WebNode(url='mock.com',
                                    children=[WebNode(url='mock.com/1'),
                                              WebNode(url='mock.com/2'),
                                              WebNode(url='mock.com/3')])

        self.assertEqual(expected_web_tree, web_crawler.root_web)

    def test_run_circular_graph(self, mock_get_webs):
        """
        Graph with circular dependency. Graph looks like this:
                        mock.com/1 - mock.com
                    /
            mock.com -  mock.com/2
                    \
                        mock.com/3
        """
        # Given
        mock_get_webs.side_effect = [['mock.com/1', 'mock.com/2', 'mock.com/3'], ['mock.com'], [], [], []]
        web_crawler = WebCrawler(url_root_web='mock.com')

        # When
        web_crawler.run()

        # Then
        node_1 = WebNode(url='mock.com/1')
        expected_web_graph = WebNode(url='mock.com',
                                     children=[node_1, WebNode('mock.com/2'), WebNode('mock.com/3')])
        node_1.children = [WebNode(url='mock.com')]

        self.assertEqual(expected_web_graph, web_crawler.root_web)
