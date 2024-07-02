import tkinter as tk
from models import Node
from ui.containers import MyFrame

class LabelNode(tk.Label):
    def __init__(self, node: Node, parent: MyFrame):
        super().__init__()
        self._parent = parent
        self._node = node
        
        self.configure(
            text=str(node.title),
            width=4,
            height=2,
            relief='flat',
            borderwidth=0
        )
        
        self.pack()
    
    @property
    def node(self) -> Node:
        return self._node
    
    @node.setter
    def node(self, value: Node):
        if not isinstance(value, Node):
            raise ValueError("Parameter must be an instance of Node.")
        self._node = value
        self.configure(text=str(value))
