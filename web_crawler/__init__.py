""" Top level package for the py-webcrawler """

__author__ = """ Patricio Tula """
__version__ = '0.1.0'

from web_crawler.web_crawler import WebCrawler
from web_crawler.web_crawler_async import WebCrawlerAsync

__all__ = (WebCrawler, WebCrawlerAsync)
