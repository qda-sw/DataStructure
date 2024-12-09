from collections import deque

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None
    def get(self, key):
        return self.get_node(self.root, key)
    def get_node(self, node, key):
        if node == None:
            return None
        if node.key > key:
            return self.get_node(node.left, key)
        elif node.key < key:
            return self.get_node(node.right, key)
        else:
            return node
    def put(self, key, value):
        self.root = self.put_node(self.root, key, value)
    def put_node(self, node, key, value):
        if node == None:
            return Node(key, value)
        if node.key > key:
            node.left = self.put_node(node.left, key, value)
        elif node.key < key:
            node.right = self.put_node(node.right, key, value)
        else:
            node.value = value
        return node
    def delete(self, key):
        self.root = self.delete_node(self.root, key)
    def delete_node(self, node, key):
        if node == None:
            return None
        if node.key > key:
            node.left = self.delete_node(node.left, key)
        elif node.key < key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            target = node
            node = self.maximum(target.left)
            node.left = self.delete_max(target.left)
            node.right = target.right
        return node
    def maximum(self, node):
        if node == None:
            return None
        if node.right == None:
            return node
        return self.maximum(node.right)
    def delete_max(self, node):
        if node == None:
            return None
        if node.right == None:
            return node.left    
        node.right = self.delete_max(node.right)
        return node
    def print(self):
        if self.root:
            self.print_node(self.root)
        else:
            print("Empty Tree")
    def print_node(self, node):
        queue = deque()
        queue.append((self.root, 0))
        while queue:
            node, depth = queue.popleft()
            print(f"{depth:<3} {node.value}")
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
