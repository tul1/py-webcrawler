from typing import List, Set

from web_crawler.models.web_node import WebNode
from web_crawler.services.web_crawler_service import WebCrawlerService


class WebCrawler(WebCrawlerService):
    def __init__(self, url_root_web: str) -> None:
        self.root_web: WebNode = WebNode(url=url_root_web)

    def run(self) -> str:
        """ Crawl the web """
        visited_webs: Set[str] = set()
        while queue := [self.root_web]:
            current_web: WebNode = queue.pop(0)
            if current_web.url.startswith(self.root_web.url) or current_web.url.startswith('/'):
                if current_web.url.startswith('/') and len(current_web.url) > 1:
                    current_web.url = self.root_web.url + current_web.url
                if current_web.url not in visited_webs:
                    visited_webs.add(current_web.url)
                    current_web.children = [WebNode(url=child_url)
                                            for child_url in WebCrawler._get_embedded_web(current_web.url)]
                    queue.extend(current_web.children)
        return repr(self.root_web)
