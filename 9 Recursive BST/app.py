class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def contains(self, curr, node):
        if curr is None:
            return False
        if curr.value == node:
            return True

        if node > curr.value:
            return self.contains(curr.right, node)
        else:
            return self.contains(curr.left, node)

    def _r_insert(self, curr, val):
        if curr is None:
            return Node(val)

        if curr.value > val:
            curr.left = self._r_insert(curr.left, val)
        if curr.value < val:
            curr.right = self._r_insert(curr.right, val)

        return curr

    def r_insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        temp = self.root
        return self._r_insert(temp, val)

    def r_contains(self, val):
        if self.root is None:
            return False

        return self.contains(self.root, val)

    def min_val(self, curr):
        while curr.left is not None:
            curr = curr.left
        return curr.value

    def __r_delete(self, curr, val):
        if curr is None:
            return None

        if curr.value > val:
            curr.left = self.__r_delete(curr.left, val)
        elif curr.value < val:
            curr.right = self.__r_delete(curr.right, val)
        else:
            if curr.left == None and curr.right == None:
                return None
            elif curr.left == None:
                curr = curr.right
            elif curr.right == None:
                curr = curr.left
            else:
                subtree_min = self.min_val(curr.right)
                curr.value = subtree_min
                curr.right = self.__r_delete(curr.right, subtree_min)
        return curr
    
    def r_delete(self, val):
        return self.__r_delete(self.root, val)


bst = BinaryTree()
bst.r_insert(10)
bst.r_insert(5)
bst.r_insert(15)  
bst.r_insert(2)
bst.r_insert(7)
print(bst.r_delete(5).left.value)