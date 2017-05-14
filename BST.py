""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    if root == None or  (root.left == None and root.right == None):
        return True

    return check_binary_search_tree_(root.left) and goMostRightNode(root.left)<root.data and check_binary_search_tree_(root.right) and getMostLeftNode(root.right)>root.data


def getMostLeftNode(root):
    if root == None:
        return 10001
    while root.left != None:
        root = root.left
    return root.data

def goMostRightNode(root):
    if root == None:
        return -1
    while root.right != None:
        root = root.right
    return root.data
