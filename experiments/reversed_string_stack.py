class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def print(self):
        return print(self.stack)

if __name__ == '__main__':
    str_ = input()
    stack = Stack()
    for i in str_:
        stack.push(i)
    for j in range(len(stack)):
        print(stack.pop(), end='')
    print()

