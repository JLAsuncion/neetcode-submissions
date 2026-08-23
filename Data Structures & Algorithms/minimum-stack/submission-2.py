class MinStack:

    
    def __init__(self):
        self.another = []
    def push(self, val: int) -> None:
        return self.another.append(val)
    def pop(self) -> None:
        return self.another.pop()
    def top(self) -> int:
        return self.another[-1]
        
    def getMin(self) -> int:
        return min(self.another)
        
