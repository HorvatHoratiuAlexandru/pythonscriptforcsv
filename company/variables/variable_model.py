class VariableModel:
    def __init__(self, type, value, fy) -> None:
        self.type = type
        self.value = value
        self.fy = fy
        
    def __str__(self):
        return f"{self.type}: {self.value}"
    
    def __repr__(self) -> str:
        return self.__str__()