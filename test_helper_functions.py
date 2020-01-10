import unittest
from helper_functions import findLCA, printKeyDepthFromNestedDict, print_key_depth_object, Node, Person

nested_dict = {
    "key1": 1,
    "key2": {
        "key3": {
            "key3": {
                "key3": {
                    "key3": {
                        "key3": {
                            "key3": {
                                "key3": {"key3": 1, "key4": {"key5": 4}},
                                "key4": {
                                    "key5": {
                                        "key3": {"key3": 1, "key4": {"key5": 4}},
                                        "key4": {"key5": 4},
                                    }
                                },
                            },
                            "key4": {"key5": {"key3": 1, "key4": {"key5": 4}}},
                        },
                        "key4": {"key5": {"key3": 1, "key4": {"key5": 4}}},
                    },
                    "key4": {"key5": {"key3": 1, "key4": {"key5": 4}}},
                },
                "key4": {"key5": {"key3": 1, "key4": {"key5": 4}}},
            },
            "key4": {"key5": 4},
        },
        "key4": {
            "key5": {
                "key3": {
                    "key3": {
                        "key3": {"key3": 1, "key4": {"key5": 4}},
                        "key4": {
                            "key5": {
                                "key3": {"key3": 1, "key4": {"key5": 4}},
                                "key4": {"key5": 4},
                            }
                        },
                    },
                    "key4": {"key5": 4},
                },
                "key4": {
                    "key5": {
                        "key3": {"key3": 1, "key4": {"key5": 4}},
                        "key4": {"key5": 4},
                    }
                },
            }
        },
    },
}


# class Node(object):
#     """docstring for Node."""

#     def __init__(self, arg):
#         super(Node, self).__init__()
#         self.arg = arg
#         self.left = None
#         self.right = None


# class Person(object):
#     def __init__(self, first_name, last_name, father):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

nested_dict_object = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": {
                "key6": {"key6": 6, "key7": {"7user": person_a}},
                "key7": {"key6": 6, "key7": {"key6": 6, "key7": 7}},
            },
            "user": person_b,
        },
    },
}


class HelperFunctionsTest(unittest.TestCase):
    def setUp(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.root = root

        self.depth_default = 0
        self.nested_dict = nested_dict
        self.nested_dict_object = nested_dict_object

    def test_findlca(self):
        print('\n === test to find lca test... ===\n')
        result = findLCA(self.root, 3, 4).arg
        self.assertEqual(result, 1)

    def test_printKeyDepthFromNestedDict(self):
        print('\n === test to print key and it\'s depth from nested dictionary... ===\n')
        printKeyDepthFromNestedDict(self.nested_dict, self.depth_default)
        pass

    def test_print_key_depth_object(self):
        print('\n === test to print key and it\'s depth of nested dictionary with object... ===\n')
        print_key_depth_object(
            self.nested_dict_object, self.depth_default)
        pass


if __name__ == "__main__":
    unittest.main()
