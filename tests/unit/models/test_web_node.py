import pytest

from unittest import TestCase

from web_crawler.models.web_node import WebNode


@pytest.mark.unit_tests
class TestWebCrawlerService(TestCase):
    def test_repr_single_node(self):
        # Given
        root = WebNode('web_1')

        # When
        webnode_repr = repr(root)

        # Then
        expected_webnode_repr = 'web_1\n'

        self.assertEqual(expected_webnode_repr, webnode_repr)

    def test_repr_simple_tree(self):
        # Given
        root = WebNode('web_1')
        web_2 = WebNode('web_2')
        web_3 = WebNode('web_3')
        web_7 = WebNode('web_7')
        web_4 = WebNode('web_4')
        web_5 = WebNode('web_5')
        web_6 = WebNode('web_6')
        root.children = [web_2, web_3, web_7]
        web_3.children = [web_4, web_6]
        web_4.children = [web_5]

        # When
        webnode_repr = repr(root)

        # Then
        expected_webnode_repr = (f'web_1\n'
                                 f'\tweb_2\n'
                                 f'\tweb_3\n'
                                 f'\t\tweb_4\n'
                                 f'\t\t\tweb_5\n'
                                 f'\t\tweb_6\n'
                                 f'\tweb_7\n')

        self.assertEqual(expected_webnode_repr, webnode_repr)
