from typing import List, Set, Dict

from web_crawler.models.web_node import WebNode
from web_crawler.services.web_crawler_service import WebCrawlerService


class WebCrawler(WebCrawlerService):
    def __init__(self, url_root_web: str) -> None:
        super().__init__(url_root_web)

    def run(self) -> str:
        """ Crawl the web """
        visited_web_nodes: Set[str] = set()
        queue: List[WebNode] = [self.root_web]
        while queue:
            current_web: WebNode = queue.pop(0)
            if current_web.url not in visited_web_nodes and current_web.url.startswith(self.root_web.url):
                visited_web_nodes.add(current_web.url)
                current_web.children = [WebNode(url=child_url) for child_url in self.get_embedded_webs(current_web.url)]
                queue.extend(current_web.children)
        return repr(self.root_web)
