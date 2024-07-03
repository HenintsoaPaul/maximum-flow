class FlowState:
    def __init__(self, start: str, end: str, plus: bool, potential: int) -> None:
        self._start: str = start
        self._end: str = end
        self._plus: bool = plus
        self._potential: int = potential
        
    @property
    def start(self) -> str:
        return self._start
    
    @property
    def end(self) -> str:
        return self._end
        
    @property
    def plus(self) -> bool:
        return self._plus
    
    @property
    def potential(self) -> int:
        return self._potential