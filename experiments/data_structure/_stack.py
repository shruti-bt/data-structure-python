
class Stack():
    def __init__(self) -> None:
        self.stack = [] 

    def push(self, value) -> None:
        self.stack.append(value)
        
    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return "{}".format(self.stack)

    def __len__(self):
        return len(self.stack)
   
        
if __name__ == "__main__":
    stack = Stack()
    stack.push(78)
    stack.push(67)
    stack.push(98)
    stack.pop()
    stack.print()

