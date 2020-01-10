# Provide a Tree of Node
# And the two of the Node(s) of it's predecessors as args
# find the Least Common Ancestor (LCA)


class Node(object):
    """docstring for Node."""

    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg
        self.left = None
        self.right = None


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


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


# Provide a Nested Dictionary
# And the default depth = 0
# Print the Key and Depth
def printKeyDepthFromNestedDict(args, depth):
    depth = depth + 1
    if len(args) > 0:
        for k, item in args.items():
            print(k, depth)
            if isinstance(item, dict):
                printKeyDepthFromNestedDict(item, depth)


# Provide a Nested Dictionary
# with also a Custom Object as children
# And the default depth = 0
# Print the Key and Depth
def print_key_depth_object(args, depth):
    depth = depth + 1
    if isinstance(args, Person):
        dict1 = vars(args)
        for o, ov in dict1.items():
            print(o, depth)
            print_key_depth_object(ov, depth)
    if isinstance(args, dict):
        if len(args) > 0:
            for k, item in args.items():
                print(k, depth)
                print_key_depth_object(item, depth)
