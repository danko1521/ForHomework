nested_list = [
    ['a', 'b', 'c'],
    [1, 2, 3, 4, 5, 6, 7, 8],
    ['d', 'e', 'f', 'h', False],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


def flat_list_yeld():
    for element in nested_list:
        if isinstance(element, list):
            for item in element:
                yield item
        else:
            yield element


for item in flat_list_yeld():
    print(item)