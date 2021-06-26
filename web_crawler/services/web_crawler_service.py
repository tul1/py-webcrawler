import requests

from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod
from typing import Generator

from web_crawler.models.web_node import WebNode
from web_crawler.utils.web_crawler_logger import WebCrawlerLogger


class WebCrawlerService(metaclass=ABCMeta):
    """ WebCrawlerService """
    @staticmethod
    def _get_embedded_web(url: str) -> Generator[str, None, None]:
        """ get embedded web """
        try:
            WebCrawlerLogger().get_logger().info(url)
            html = requests.get(url).text
            soup = BeautifulSoup(html, features='html5lib')
        except Exception as e:
            WebCrawlerLogger().get_logger().warn(f'{url} coud not be parse due to: {e}')
            return None
        else:
            for a_tag in soup.find_all('a'):
                yield a_tag.get('href')

    @abstractmethod
    def run(self) -> str:
        """ run method """
        raise NotImplementedError
