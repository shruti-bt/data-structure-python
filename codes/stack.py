class Stack():
    def __init__(self) -> None:
        self.stack = [] 

    def push(self, value) ->None:
        self.stack.append(value)
        
    def pop(self):
        self.stack.pop()

    def print(self):
        return print(*self.stack, sep=" --> ")
        

if __name__ == "__main__":
    stack = Stack()
    stack.push(78)
    stack.push(67)
    stack.push(98)
    stack.pop()
    stack.print()

