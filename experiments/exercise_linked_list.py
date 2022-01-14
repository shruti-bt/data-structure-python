class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data = data, next = self.head)
        self.head = node

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print(self):
        if self.head is None:
            print("Your Linked List is empty.")
        else:
            itr = self.head
            str_list = ""
            while itr:
                str_list += str(itr.data) + " -> "
                itr = itr.next
            print(str_list[:-4]+".")

if __name__ == "__main__":
    my_list = LinkedList()
    # # my_list.print()
    my_list.insert_at_beginning("mango")
    my_list.insert_at_beginning("orange")
    my_list.insert_at_beginning("apple")
    my_list.insert_after_value("mango", "banana")
    my_list.remove_by_value("orange")
    my_list.print()