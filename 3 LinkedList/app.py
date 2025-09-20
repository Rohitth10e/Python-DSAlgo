class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        print("head -> ", end="")
        while temp is not None:
            print(f"{temp.value} -> ",end="")
            temp = temp.next
        print("NULL ", end="")

    def append(self,value):
        node = Node(value)
        if self.head == None or self.tail == None:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1
        return True

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.print_list()
print(f"\ntail element: {linked_list.tail.value}\nLength of Linked list: {linked_list.length}")