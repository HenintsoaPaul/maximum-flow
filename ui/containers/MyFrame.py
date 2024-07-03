import tkinter as tk
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
        
        self.setup_ui(width=width, height=height, bg=bg, title=title, tool_frame_height=50)
        self.setup_listeners()
        
        self.setup_content()
        
    def setup_listeners(self) -> None:
        def on_click() -> None:
            print("Looking for a way to increment the flow...")
            print(f"Current flow: {self.graph.get_curr_flow()}")
            flow_states = self.graph.get_flow_states(node_title='S', flow_states=[])
            self.graph.increment_graph(flow_states)
            print(f"Current flow: {self.graph.get_curr_flow()}\n")
            self.update_canvas()
            
        btn_ok = tk.Button(self._tool_frame, text="Gooo!", command=on_click)
        btn_ok.pack(side=tk.LEFT)
        
        btn_save = tk.Button(self._tool_frame, text="Save", command=self.save_label_nodes_position)
        btn_save.pack(side=tk.LEFT)
        
        btn_load = tk.Button(self._tool_frame, text="Load", command=self.load_label_nodes_position)
        btn_load.pack(side=tk.LEFT)
        
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
    
    def save_label_nodes_position(self) -> None:
        # Save the position of each label node in a JSON file
        positions = {}
        for label_node in self.list_label_nodes:
            positions[label_node.node] = (label_node.winfo_x(), label_node.winfo_y())
        
        import json
        with open('label_nodes_positions.json', 'w') as file:
            json.dump(positions, file)
            
    def load_label_nodes_position(self) -> None:
        # Load the position of each label node from a JSON file
        import json
        with open('label_nodes_positions.json', 'r') as file:
            positions = json.load(file)
            
        for label_node in self.list_label_nodes:
            x, y = positions[label_node.node]
            label_node.place(x=x, y=y)
            
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
