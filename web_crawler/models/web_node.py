
from __future__ import annotations
from typing import Optional, List, Set


class WebNode:
    def __init__(self, url: str, children: Optional[List[WebNode]] = None) -> None:
        self.url: str = url
        self.children: List[WebNode] = children or list()

    @staticmethod
    def _print_webs_dfs(root: WebNode, output: str, depth: int, visited: Set[str]) -> str:
        depth += 1
        if root.url not in visited:
            visited.add(root.url)
            for child in root.children:
                output += '\t' * depth + WebNode._print_webs_dfs(child, child.url + '\n', depth, visited)
        return output

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __repr__(self) -> str:
        """ representation opetator """
        return WebNode._print_webs_dfs(self, self.url + '\n', 0, set())
