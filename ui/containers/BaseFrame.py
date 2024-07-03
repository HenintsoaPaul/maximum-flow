import tkinter as tk

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
        
    def draw_line(self, label_1: tk.Label, label_2: tk.Label, color: str, width: int, tags: str) -> None:
        x1, y1 = label_1.winfo_x(), label_1.winfo_y()
        x2, y2 = label_2.winfo_x(), label_2.winfo_y()
        
        # print(f"Draw line from ({x1}, {y1}) to ({x2}, {y2})")
        self._canvas.create_line(x1, y1, x2, y2, fill=color, width=width, tags=tags)
