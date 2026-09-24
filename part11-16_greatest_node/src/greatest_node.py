# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    node_sum = root.value

    if root.left_child is not None:
        node_sum = max(node_sum, greatest_node(root.left_child))

    if root.right_child is not None:
        node_sum = max(node_sum, greatest_node(root.right_child))

    return node_sum