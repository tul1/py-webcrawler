from typing import List, Set, Any, Coroutine

from web_crawler.models.web_node import WebNode
from web_crawler.services.web_crawler_service import WebCrawlerService


class WebCrawlerAsync(WebCrawlerService):
    def __init__(self, url_root_web: str) -> None:
        self._root_web: WebNode = WebNode(url=url_root_web)

    def run(self) -> str:
        """ Crawl the web """
        queue: List[WebNode] = [self._root_web]
        visited_webs: Set[WebNode] = set()
        while queue:
            current_web: WebNode = queue.pop(0)
            if current_web not in visited_webs:
                visited_webs.add(current_web)
                current_web.children = [WebNode(url=child_url)
                                        for child_url in self.get_embedded_webs(current_web.url)]
                queue.extend(current_web.children)
        return repr(self._root_web)
