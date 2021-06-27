import pytest

from unittest import TestCase

from web_crawler.utils.singleton import Singleton


class FakeClass(metaclass=Singleton):
    pass


@pytest.mark.unit_tests
class TestSingleton(TestCase):

    def test_is_singleton(self):
        # When
        first = FakeClass()
        second = FakeClass()

        # Then
        assert first is second
