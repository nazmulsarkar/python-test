class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

nested_dict = {
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

# define default depth
depth_default = 0


def print_key_depth(args, depth):
    depth = depth + 1
    if isinstance(args, Person):
        dict1 = vars(args)
        for o, ov in dict1.items():
            print(o, depth)
            print_key_depth(ov, depth)
    if isinstance(args, dict):
        if len(args) > 0:
            for k, item in args.items():
                print(k, depth)
                print_key_depth(item, depth)


print_key_depth(nested_dict, depth_default)
