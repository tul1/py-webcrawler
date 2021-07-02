import requests

from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod
from typing import Generator, Any, Set

from web_crawler.models.web_node import WebNode
from web_crawler.utils.web_crawler_logger import WebCrawlerLogger


class WebCrawlerService(metaclass=ABCMeta):
    """ WebCrawlerService """
    def get_embedded_webs(self, url: str) -> Generator[str, None, None]:
        """ get embedded web """
        self._visited_node: Set = set()
        try:
            WebCrawlerLogger().get_logger().info(url)
            html = requests.get(url).text
            soup = BeautifulSoup(html, features='html5lib')
        except Exception as e:
            WebCrawlerLogger().get_logger().warning(f'{url} coud not be parse due to: {e}')
            return None
        else:
            formatted_urls = map(lambda a: self._format_url(a), soup.find_all('a')) 
            yield from filter(None, formatted_urls)

    def _format_url(self, a: Any) -> str:
        url: str = a.get('href')
        if url and url not in self._visited_node:
            self._visited_node.add(url)
            if url.startswith('http'):
                return url
            elif url.startswith('/'):
                url = self.root_web.url + url[1:]
                self._visited_node.add(url)
                return url
        return None

    @abstractmethod
    def run(self) -> str:
        """ run method """
        raise NotImplementedError
