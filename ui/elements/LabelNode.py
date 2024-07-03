import tkinter as tk
from ui.containers import MyFrame

class LabelNode(tk.Label):
    def __init__(self, node: str, parent: MyFrame):
        super().__init__(parent, text=str(node), width=4, height=2)
        self.configure(borderwidth=0, relief="solid")
        
        self._parent: MyFrame = parent
        self._node: str = node
        
    @property
    def node(self) -> str:
        return self._node
    
    @node.setter
    def node(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Parameter must be an instance of str.")
        self._node = value
        self.configure(text=str(value))
