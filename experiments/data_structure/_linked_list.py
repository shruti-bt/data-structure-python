
class Node():
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head) 
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data=data, next=None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data=data, next=None)
    
    
    def __len__(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
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

    
    def __str__(self):
        if self.head is None:
            return "Your Linked List is empty."
        else:
            itr = self.head
            str_list = ""
            while itr:
                str_list += str(itr.data) + " -> "
                itr = itr.next
            return str_list[:-4]+"."

        

# Node is denoted by `{}`
if __name__ == "__main__":
    mylist = LinkedList() # empty list created. where head == None
    print(mylist) # it will print empty list.
    mylist.insert_at_beginning(99) # head (99) == {data: 99, next: None}
    mylist.insert_at_beginning(40) # head (40) == {data: 40, next: {data: 99, next: None}}
    mylist.insert_at_end(90)# head (40) == {data: 40, next: {data: 99, next: {data: 90, next: None}}}
    mylist.insert_after_value(40, 76)
    mylist.remove_by_value(99)
    print(len(mylist))
    print(mylist) # print 3 elements 40 --> 76 --> 90




