class Node:
    def __init__(self,value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
root = Node(1)
left = Node(2)
right = Node(3)
left_left = Node(4)
left_right = Node(5)
root.left = left
root.right = right
left.parent = root
left.left = left_left
left.right = left_right
right.parent = root

def insert(node: Node, x): #TODO: Add a helper method!!!!!!!!!!!!!!!!!!!!!!!!
    if node is None:
        return
    if x < node:
        pass
    # Add the value
    # Change the new node
    # Recursively do insert

# COUNT EACH NODE IN THE TREE
def count(node:Node):
    if node is None:
        return 0
    else:
        return 1 + count(node.left) + count(node.right)
print(count(root))

# def mirror(self):
#     mirror_h(self.root)
# def mirror_h(current: Node):
#     if current is None:
#         return
#     current.left,current.right = current.right,current.left
#     mirror_h(current.left)
#     mirror_h(current.right)
# mirror(root.value)