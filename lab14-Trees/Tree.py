class Tree:
    def __init__(self):
        self.parent = Node
        self.children = [Node]

    def create_tree(self, child):
        self.parent = self
        self.children.append(child)

class Node:
    def __init__(self):
        self.data = Tree
        self.left = Node
        self.right = Node