import tkinter as tk
from models import Node
from ui.containers import MyFrame

class LabelNode(tk.Label):
    """
    Une étiquette qui affiche des informations sur un noeud spécifique.
    
    Attributes:
        _parent (tk.Frame): Le conteneur parent de l'étiquette.
        _node (Node): L'objet Node associé à l'étiquette.
    """
    
    def __init__(self, node: Node, parent: MyFrame):
        super().__init__()
        self._parent = parent
        self._node = node
        
        self.configure(text=str(node.title))
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
