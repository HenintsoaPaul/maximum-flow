from models.Graph import Graph
from ui.elements.LabelNode import LabelNode
from ui.behavior.Draggable import Draggable
from ui.containers.BaseFrame import BaseFrame

class MyFrame(BaseFrame):
    def __init__(self, width: int, height: int, bg: str, title: str) -> None:
        super().__init__()
        
        self.list_label_nodes: list[LabelNode] = []
        self.graph: Graph = Graph(head_title='S', tail_title='P')
        self.graph.initialize_data()
        
        self.setup_ui(width=width, height=height, bg=bg, title=title)
        self.setup_content()
        
    def setup_content(self) -> None:
        """Initialise le contenu à afficher."""
        
        # Create label nodes
        for node_title in self.graph._body:
            label_node = LabelNode(node=node_title, parent=self)
            self.list_label_nodes.append(label_node)
            Draggable(widget=label_node, my_frame=self, x=0, y=0, update_canvas_callback=self.update_canvas)
            
        self.draw_connections()
                                     
    def get_label_node(self, node_title: str) -> LabelNode:
        for label_node in self.list_label_nodes:
            if label_node.node == node_title:
                return label_node
        return None
            
    def update_canvas(self) -> None:
        print("Updating canvas...")
        self.draw_connections()
        
    def draw_connections(self) -> None:
        self.Canvas.delete('conx')
        self.Canvas.delete('flow')
        self.Canvas.delete('capacity')
        
        for label_node in self.list_label_nodes:
            if not self.graph._tail_title == label_node.node:
                for node_link in self.graph._body[label_node.node]:
                    if node_link.forward:
                        self.draw_line(
                            label_1=label_node, 
                            label_2=self.get_label_node(node_link.node),
                            tags='conx', 
                            flow=node_link.flow, capacity=node_link.capacity
                        )
