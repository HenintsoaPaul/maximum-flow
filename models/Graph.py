from typing import Dict, Set
from models.NodeLink import NodeLink


class Graph:
    def __init__(self, head_title: str, tail_title: str) -> None:
        self._head_title: str = head_title
        self._tail_title: str = tail_title
        self._body: Dict[str, Set[NodeLink]] = {}
        
    def initialize_data(self) -> None:
        self._body = {
            'S': {
                NodeLink('A', capacity=10, flow=7, forward=True),
                NodeLink('D', capacity=20, flow=20, forward=True),
                NodeLink('G', capacity=20, flow=11, forward=True)
            },
            'A': {
                NodeLink('S', capacity=10, flow=7, forward=False),
                NodeLink('B', capacity=5, flow=3, forward=True),
                NodeLink('E', capacity=4, flow=4, forward=True)
            },
            'B': {
                NodeLink('A', capacity=5, flow=3, forward=False),
                NodeLink('C', capacity=4, flow=4, forward=True),
                NodeLink('E', capacity=2, flow=1, forward=False)
            },
            'C': {
                NodeLink('B', capacity=4, flow=4, forward=False),
                NodeLink('E', capacity=9, flow=4, forward=False),
                NodeLink('F', capacity=8, flow=0, forward=True),
                NodeLink('P', capacity=8, flow=8, forward=True)
            },
            'F': {
                NodeLink('P', capacity=30, flow=20, forward=True)
            }
        }
    
    def get_neighbors(self, node_title: str) -> Set[NodeLink]:
        try:
            return self._body[node_title]
        except KeyError:
            msg = f"No links found for node titled '{node_title}'."
            raise KeyError(msg)
        
    def get_forward_neighbors(self, node_title: str) -> Set[NodeLink]:
        neighbors = self.get_neighbors(node_title)
        return {node_link for node_link in neighbors if node_link.forward}
        
    def get_unvisited_neighbors(self, node_title: str) -> Set[NodeLink]:
        neighbors = self.get_neighbors(node_title)
        return {node_link for node_link in neighbors if not node_link.visited}
    
    def get_free_neighbors(self, node_title: str) -> Set[NodeLink]:
        """Retourne les voisins qui sont libres, cad non visites et flow non maximal."""
        
        neighbors = self.get_neighbors(node_title)
        return {node_link for node_link in neighbors if node_link.is_free}
    
    def get_curr_flow(self) -> int:
        """Permet d'obtenir le flow actuel de la graphe."""
        
        curr_flow: int = 0
        for node_link in self._body[self._head_title]:
            curr_flow += node_link.flow
        return curr_flow