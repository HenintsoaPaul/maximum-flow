import tkinter as tk
from models.Node import Node
from ui.elements.LabelNode import LabelNode
from ui.behavior.Draggable import Draggable
from ui.containers.BaseFrame import BaseFrame

class MyFrame(BaseFrame):
    def __init__(self, width: int, height: int, bg: str, title: str) -> None:
        super().__init__()
        
        self._list_nodes: list[Node] = []
        self._list_label_nodes: list[LabelNode] = []
        
        self.setup_ui(width=width, height=height, bg=bg, title=title)
        self.setup_content()
        
    def setup_content(self) -> None:
        """Initialise le contenu à afficher."""
        data = [
            Node(title='A'),
            Node(title='B')
        ]
        for node in data:
            label_node = LabelNode(node=node, parent=self)
            self._list_label_nodes.append(label_node)
            Draggable(widget=label_node, my_frame=self, x=15, y=15, update_canvas_callback=self.update_canvas)
            
    def update_canvas(self) -> None:
        print("Updating canvas...")
