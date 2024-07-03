import tkinter as tk
from ui.elements.LabelNode import LabelNode

class BaseFrame(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
    
    @property
    def Width(self) -> int:
        return self._width
    
    @property
    def Height(self) -> int:
        return self._height
    
    @property
    def Bg(self) -> str:
        return self._bg
    
    @property
    def Canvas(self) -> tk.Canvas:
        return self._canvas
    
    def setup_ui(self, width: int, height: int, bg: str, title: str) -> None:
        def setup_container(self, width: int, height: int, bg: str) -> None:
            """Configure le conteneur principal."""
            self._bg = bg
            self._width = width
            self._height = height
        
        def setup_main_frame(self) -> None:
            """Configure la frame principale"""
            self._main_frame = tk.Frame(
                self, 
                width=self.Width, 
                height=self.Height, 
                bg=self.Bg
            )
            self._main_frame.pack()

        def setup_canvas(self) -> None:
            """Initialise le canevas pour le dessin."""
            self._canvas = tk.Canvas(
                self._main_frame, 
                width=self.Width, 
                height=self.Height,
                bg=self.Bg
            )
            self._canvas.pack()
    
        setup_container(self, width=width, height=height, bg=bg)
        setup_main_frame(self)
        setup_canvas(self)
        
        self.title(title)
        self.geometry(f"{self.Width + 10}x{self.Height + 10}")
        self.resizable(False, False)
        
        
    def draw_line(self, label_1: LabelNode, label_2: LabelNode, flow: int, capacity: int, tags: str) -> None:
        # Line
        x1, y1 = label_1.winfo_x(), label_1.winfo_y()
        x2, y2 = label_2.winfo_x(), label_2.winfo_y()
        self.Canvas.create_line(x1, y1, x2, y2, fill="black", width=2, tags=tags)
        
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        
        # Text flow
        self.Canvas.create_text(x_center, y_center - 5, text=flow, fill="red", tags="flow", font=("Cascadia Code", 15))
        
        # Text capacity
        self.Canvas.create_text(x_center, y_center + 15, text=capacity, fill="blue", tags="capacity", font=("Cascadia Code", 15))
