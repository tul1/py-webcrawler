import logging

from web_crawler.utils.singleton import Singleton


class WebCrawlerLogger(metaclass=Singleton):

    def __init__(self):
        self._logger = logging.getLogger('web-crawler')
        self._logger.setLevel(logging.DEBUG)
        # create formatter and add it to the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s')
        # create console handler with a higher log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)

    def get_logger(self):
        return self._logger
