class DoubleQueue():
    def __init__(self):
        self._double_queue = []

    def push_at_beginning(self, value):
        self._double_queue.insert(0, value)

    def push_at_end(self, value):
        self._double_queue.append(value)

    def pop_from_beginning(self):
        self._double_queue.pop(0)

    def pop_from_end(self):
        self._double_queue.pop()
    
    def print(self):
        return print(self._double_queue)

if __name__ == "__main__":
    doublequeue = DoubleQueue()
    doublequeue.push_at_beginning(67)
    doublequeue.push_at_beginning(60)
    doublequeue.push_at_beginning(78)
    doublequeue.push_at_end(56)
    doublequeue.pop_from_beginning()
    doublequeue.pop_from_end()
    doublequeue.print()




    



