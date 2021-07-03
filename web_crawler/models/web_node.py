
from __future__ import annotations
from typing import Optional, List, Set


class WebNode:
    def __init__(self, url: str, children: Optional[List[WebNode]] = None) -> None:
        self.url: str = url
        self.children: List[WebNode] = children or list()

    def _print_webs_dfs(root: WebNode, output: str, depth: int) -> str:
        for child in root.children:
            output += '\t' * depth + WebNode._print_webs_dfs(child, child.url + '\n', depth + 1)
        return output

    def __eq__(self, other) -> bool:
        return repr(self) == repr(other)

    def __repr__(self) -> str:
        """ representation opetator """
        return WebNode._print_webs_dfs(self, self.url + '\n', 1)
