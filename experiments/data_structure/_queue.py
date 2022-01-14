

class Queue:
    
    def __init__(self) -> None:
        self._queue = []
    
    def insert(self, val: int) -> None:
        self._queue.append(val)

    def pop(self) -> None:
        self._queue.pop(0)

    def print(self) -> None:
        return print(self._queue, sep=" --> ")

    def __len__(self):
        return len(self._queue)

    
if __name__ == "__main__":
    queue = Queue()
    queue.print()
    queue.insert(10)
    queue.insert(53)
    queue.pop()
    queue.insert(48)
    queue.print()
    print(len(queue))
