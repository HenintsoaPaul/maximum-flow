class FlowState:
    def __init__(self, plus: bool, potential: int) -> None:
        self._plus: bool = plus
        self._potential: int = potential
        
    @property
    def plus(self) -> bool:
        return self._plus
    
    @property
    def potential(self) -> int:
        return self._potential