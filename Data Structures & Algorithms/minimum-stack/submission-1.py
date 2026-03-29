class MinStack:

    def __init__(self):
        
        self.valstack= []
        self.minstack= []

    def push(self, val: int) -> None:
        self.valstack.append(val)
        min_val= min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(min_val)

    def pop(self) -> None:
        self.valstack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.valstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
