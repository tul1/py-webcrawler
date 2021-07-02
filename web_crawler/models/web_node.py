
from __future__ import annotations
from typing import Optional, List, Set


class WebNode:
    def __init__(self, url: str, children: Optional[List[WebNode]] = None) -> None:
        self.url: str = url
        self.children: List[WebNode] = children or list()

    @staticmethod
    def add_child(nodes_table: Dict[str, WebNode], node: WebNode, child_url: str) -> None:
        """ Add child to node """
        if nodes_table.get(child_url):
            node.children.append(nodes_table[child_url])
        else:
            new_node = WebNode(url=child_url)
            node.children.append(new_node)
            nodes_table[child_url] = new_node

    @staticmethod
    def _print_webs_dfs(root: WebNode, output: str, depth: int, visited: Set[str]) -> str:
        depth += 1
        if root.url not in visited:
            visited.add(root.url)
            for child in root.children:
                output += '\t' * depth + WebNode._print_webs_dfs(child, child.url + '\n', depth, visited)
        return output

    def __eq__(self, other):
        return self.url == other.url

    def __repr__(self) -> str:
        """ representation opetator """
        return WebNode._print_webs_dfs(self, self.url + '\n', 0, set())
