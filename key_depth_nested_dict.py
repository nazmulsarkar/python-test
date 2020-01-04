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
depth_default = 0


def print_key_depth(args, depth):
    depth = depth + 1
    if len(args) > 0:
        for k, item in args.items():
            print(k, depth)
            if isinstance(item, dict):
                print_key_depth(item, depth)


print_key_depth(nested_dict, depth_default)
