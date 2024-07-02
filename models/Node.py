class Node:
    def __init__(self, title: str) -> None:
        self._title = title
        
    @property
    def title(self) -> str:
        return self._title