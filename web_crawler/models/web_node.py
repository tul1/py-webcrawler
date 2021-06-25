
from __future__ import annotations
from typing import Optional, List


class WebNode:
    def __init__(self, url: str, children: Optional[List[WebNode]] = None) -> None:
        self.url: str = url
        self.children: List[WebNode] = children or list()
    
    def __eq__(self, other: WebNode) -> bool:
        """ equals operator """
        return self.url == other.url

    def __repr__(self) -> str:
        """ representation opetator """
        return self.url
