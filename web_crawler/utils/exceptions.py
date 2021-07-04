from web_crawler.utils.web_crawler_logger import WebCrawlerLogger


class WebCrawlerException(Exception):

    def __init__(self, message):
        super().__init__(self)
        WebCrawlerLogger().get_logger().error(message)
        self.message = message
