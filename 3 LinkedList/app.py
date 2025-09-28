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
            print(f"{temp.value} -> ", end="")
            temp = temp.next
        print("NULL ", end="")

    def is_empty(self):
        return self.length == 0

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    # def pop(self):
    #     if self.head is None:
    #         print("LinkedList is empty")
    #         return
    #     if self.head == self.tail:
    #         self.head = None
    #         self.tail = None
    #     else:
    #         temp = self.head
    #         while temp.next is not self.tail:
    #             temp = temp.next
    #         temp.next = None
    #         self.tail = temp
    #         self.length -=1
    #     return True

    def pop(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            prev, temp = self.head, self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
            popped_node = self.tail
            self.tail = prev
            self.tail.next = None
            self.length -= 1
        print(f"\npopped_node: {popped_node.value}")

    # def pop2(self):
    #     if not self.is_empty():
    #         temp = self.head
    #         while temp.next is not self.tail:
    #             temp = temp.next
    #         temp.next = None
    #         self.tail = temp
    #     elif self.head == self.tail:
    #         self.head = None
    #         self.tail = None
    #     self.length -= 1

    def prepend(self, value):
        new_node = Node(value)
        # self.head is None or self.length == 0:
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # def pop_first(self):
    #     if self.is_empty():
    #         print("\nLinked list is empty\n")
    #         return None
    #     temp=self.head

    #     if self.head == self.tail:
    #         self.head =  None
    #         self.tail = None
    #     else:
    #         self.head = self.head.next
    #     self.length -=1
    #     print(f"\nPopped first element: {temp.value}\n")

    def pop_first(self):
        if self.is_empty():
            print("\nLinked list is empty\n")
            return None

        temp = self.head

        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        print(f"\nPopped first element: {temp.value}\n")
        return temp

    def get(self, index):
        if self.is_empty() or index < 0 or self.length <= index:
            return None

        temp = self.head

        # while temp is not None:
        #     if idx == index:
        #         return temp.value
        #     idx+=1
        #     temp = temp.next
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, idx, value):
        temp = self.get(idx)

        if temp:
            temp.value = value
            return True
        return False

    # def insert(self, idx, value):
    #     new_node = Node(value)

    #     if idx < 0 or idx > self.length:
    #         return None
    #     if idx == 0:
    #         new_node.next = self.head
    #         self.head = new_node
    #         if self.length == 0:
    #             self.tail = new_node
    #     else:
    #         temp = self.get(idx-1)
    #         new_node.next = temp.next
    #         temp.next = new_node
    #         if self.length == idx:
    #             self.tail = new_node
    #     self.length+=1
    #     return True

    def insert(self, idx, value):
        if idx < 0 or idx > self.length:
            return False

        if idx == 0:
            return self.prepend(value)
        elif idx == self.length:
            return self.append(value)

        new_node = Node(value)
        prev = self.get(idx - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def reverse(self):
        self.head, self.tail = self.tail, self.head
        temp = self.tail
        before = None
        after = temp.next

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.print_list()

popped = linked_list.pop()
linked_list.print_list()

linked_list.prepend(3)
linked_list.print_list()

print("\n", linked_list.get(1).value)
linked_list.set(1, 4)
linked_list.print_list()

linked_list.insert(2, 5)
print(f"\nlength: {linked_list.length}")
linked_list.print_list()
linked_list.reverse()
linked_list.print_list()
