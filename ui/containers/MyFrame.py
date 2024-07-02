import tkinter as tk
from models.Node import Node
from ui.elements.LabelNode import LabelNode
from ui.behavior.Draggable import Draggable

class MyFrame(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        
        self._list_nodes: list[Node] = []
        self._list_label_nodes: list[LabelNode] = []
        
        self.setup_ui()
        self.setup_content()
        
    @property
    def Width(self) -> int:
        return self._width
    
    @property
    def Height(self) -> int:
        return self._height
    
    @property
    def Canvas(self) -> tk.Canvas:
        return self._canvas 

    def setup_ui(self) -> None:
        def setup_container(self, width: int, height: int, bg: str) -> None:
            """Configure le conteneur principal."""
            self._bg = bg
            self._width = width
            self._height = height
        
        def setup_main_frame(self) -> None:
            """Configure la frame principale"""
            self._main_frame = tk.Frame(self, width=self.Width, height=self.Height, bg='red')
            self._main_frame.pack()

        def setup_canvas(self) -> None:
            """Initialise le canevas pour le dessin."""
            self._canvas = tk.Canvas(
                self._main_frame, 
                width=self._width, 
                height=self._height,
                bg=self._bg
            )
    
        setup_container(self, width=800, height=500, bg="yellow")
        setup_main_frame(self)
        setup_canvas(self)
        
        self.title('Flow Max')
        self.geometry(f"{self.Width + 10}x{self.Height + 10}")
        self.resizable(False, False)
        
    def setup_content(self) -> None:
        """Initialise le contenu à afficher."""
        data = [
            Node(title='A'),
            Node(title='B')
        ]
        for node in data:
            # self._list_nodes.append(node)
            label_node = LabelNode(node=node, parent=self)
            self._list_label_nodes.append(label_node)
            Draggable(widget=label_node, my_frame=self, x=15, y=15, update_canvas_callback=self.update_canvas)
            
    def update_canvas(self) -> None:
        """Méthode appelée pour mettre à jour le canevas."""
        print("Updating canvas...")
