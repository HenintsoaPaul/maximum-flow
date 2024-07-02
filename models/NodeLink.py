from models.Node import Node

class NodeLink:
    def __init__(self, node_title: str, capacity: int, flow: int, forward: bool) -> None:
        self._node: Node = Node(title=node_title)
        self._capacity: int = capacity
        self._flow: int = flow
        self._forward: bool = forward
        self._visited: bool = False

    @property
    def node(self) -> Node:
        return self._node

    @node.setter
    def node(self, value: Node) -> None:
        if not isinstance(value, Node):
            raise ValueError("Value must be an instance of Node.")
        self._node = value

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Capacity must be an integer.")
        self._capacity = value

    @property
    def flow(self) -> int:
        return self._flow

    @flow.setter
    def flow(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Flow must be an integer.")
        self._flow = value

    @property
    def forward(self) -> bool:
        return self._forward

    @forward.setter
    def forward(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("Forward must be a boolean.")
        self._forward = value
