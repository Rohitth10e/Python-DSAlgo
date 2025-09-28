class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def is_empty(self):
        return self.length == 0

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value,"-> ", end="")
            temp = temp.next
        print("None")

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length+=1


if __name__ == "__main__":
    d_list = DoublyLinkedList(1)
    d_list.append(2)
    d_list.printList()

