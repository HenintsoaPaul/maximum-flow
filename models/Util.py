from typing import Set
from models.Graph import Graph

class Util:
    @staticmethod
    def dfs(graph: Graph, node_title: str, accumulated_flow: int=0, visited: Set[str]=None):
        if visited is None:
            visited = set()

        if node_title in visited:
            return

        # Process the current node
        accumulated_flow += graph.get_node(node_title).flow
        visited.add(node_title)

        for neighbor in graph._body[node_title]:
            Util.dfs(graph, neighbor.node.title, accumulated_flow, visited)
            
        return accumulated_flow