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
        return True
    
    def pop(self):
        if self.is_empty():
            return False
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.is_empty():
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return True
    
    def get(self,idx):
        if self.is_empty() or idx >= self.length or 0 > idx:
            return None
        
        if idx <= self.length//2:
            temp = self.head
            for _ in range(idx):
                temp=temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, idx, -1):
                temp = temp.prev
        return temp
    
    def insert(self,value,idx):
        if idx < 0 or idx > self.length:
            return None


        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
            self.length +=1
        elif idx == 0:
            return self.prepend(value)
        elif idx == self.length:
            return self.append(value)
        else:
            # if idx <= self.length//2:
            #     temp = self.head
            #     for _ in range(idx):
            #         temp = temp.next
            # else:
            #     temp = self.tail
            #     for _ in range(self.length-1, idx, -1):
            #         temp = temp.prev
            # temp = self.get(idx)
            # new_node.next = temp
            # temp.prev.next = new_node
            # new_node.prev = temp.prev
            # temp.prev = new_node
            after = self.get(idx)
            before = after.prev
            before.next = new_node
            new_node.prev = before
            after.prev = new_node
            new_node.next = after
            self.length +=1
        return True
    
    def set(self,value,idx):
        if self.is_empty() or idx < 0 or idx >= self.length:
            return None
        
        temp = self.get(idx)
        if temp:
            temp.value = value
            return True
        return False

    def remove(self, idx):
        if self.is_empty() or idx < 0 or idx >= self.length:
            return None

        if idx == 0:
            return self.pop_first()
        elif idx == self.length-1:
            return self.pop()
        else:
            before = self.get(idx-1)
            after = before.next
            before.next = after.next
            after.prev = before
            self.length-=1
        return True

if __name__ == "__main__":
    d_list = DoublyLinkedList(1)
    d_list.append(2)
    d_list.pop()
    d_list.prepend(3)
    d_list.pop_first()
    d_list.printList()
    idx=1
    # print(f"element : {d_list.get(idx).value} at index: {idx}")
    print(f"element : {d_list.insert(8,idx)} at index: {idx}")
    d_list.set(9,1)
    d_list.remove(1)
    d_list.printList()
    # print(f"Head {d_list.head.value}")

