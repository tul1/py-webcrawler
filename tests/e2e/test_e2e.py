import pytest

from unittest import TestCase

from web_crawler.web_crawler import WebCrawler


@pytest.mark.e2e_tests
class TestE2E(TestCase):

    def test_2e2(self):
        # Given
        crawler = WebCrawler('http://lci.labi.fi.uba.ar/')

        # When
        web = crawler.run()

        # Then
        expected_web = ''

        assert(expected_web, web)
