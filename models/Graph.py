from models.NodeLink import NodeLink

class Graph:
    def __init__(self, head_title: str, tail_title: str) -> None:
        self._head_title: str = head_title
        self._tail_title: str = tail_title
        self._body: {str, set[NodeLink]} = {}
    
    def get_neighbors(self, node_title: str) -> set[NodeLink]:
        try:
            return self._body[node_title]
        except KeyError:
            msg = f"No links found for node titled '{node_title}'."
            raise KeyError(msg)
        
    def get_unvisited_neighbors(self, node_title: str) -> set[NodeLink]:
        neighbors = self.get_neighbors(node_title)
        return {node_link for node_link in neighbors if not node_link.visited}
        
    def set_data(self) -> None:
        self._body = self.get_data()
    
    def get_data(self) -> {str, set[NodeLink]}:
        return {
            'S': set([
                NodeLink('A', capacity=10, flow=7, forward=True),
                NodeLink('D', capacity=20, flow=20, forward=True),
                NodeLink('G', capacity=20, flow=11, forward=True)
            ]),
            'A': set([
                NodeLink('S', capacity=10, flow=7, forward=False),
                NodeLink('B', capacity=5, flow=3, forward=True),
                NodeLink('E', capacity=4, flow=4, forward=True)
            ]),
            'B': set([
                NodeLink('A', capacity=5, flow=3, forward=False),
                NodeLink('C', capacity=4, flow=4, forward=True),
                NodeLink('E', capacity=2, flow=1, forward=False)
            ]),
            'C': set([
                NodeLink('B', capacity=4, flow=4, forward=False),
                NodeLink('E', capacity=9, flow=4, forward=False),
                NodeLink('F', capacity=8, flow=0, forward=True),
                NodeLink('P', capacity=8, flow=8, forward=True)
            ]),
            'F': set([
                NodeLink('P', capacity=30, flow=20, forward=True)
            ])
        }