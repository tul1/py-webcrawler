import requests

from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod
from typing import Generator

from web_crawler.models.web_node import WebNode
from web_crawler.utils.exceptions import WebCrawlerException


class WebCrawlerService(metaclass=ABCMeta):
    """ WebCrawlerService """
    @staticmethod
    def _get_embedded_web(url: str) -> Generator[str, None, None]:
        """ get embedded web """
        try:
            html = requests.get(url).text
            soup = BeautifulSoup(html)
        except Exception:
            raise WebCrawlerException(f'{url} does not have a web site.'
                                      f'Request failed or html could not be parse.')
        else:
            for a_tag in soup.find_all('a'):
                yield a_tag.get('href')

    @abstractmethod
    def run(self) -> str:
        """ run method """
        raise NotImplementedError
