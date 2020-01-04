# At first create Node consructor
class Node(object):
    """docstring for Node."""

    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    if root is None:
        return None

    if root.arg == n1 or root.arg == n2:
        return root

    leftLCA = findLCA(root.left, n1, n2)
    rightLCA = findLCA(root.right, n1, n2)

    if leftLCA and rightLCA:
        return root

    return leftLCA if leftLCA is not None else rightLCA


# test the logic
# create the root node at first
# then some of the predecessors
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(findLCA(root, 3, 4).arg)
