nested_list = [
    ['a', 'b', 'c'],
    [1, 2, 3, 4, 5, 6, 7, 8],
    ['d', 'e', 'f', 'h', False],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


class FlatList(list):

    def __iter__(self):
        return self

    def __next__(self):
        list_of_list = []
        if len(self) == 0:
            raise StopIteration
        else:
            list_of_list.append(self.pop(0))

        list_of_element = []
        for element in list_of_list[0]:
            list_of_element.append(element)
        return list_of_element


not_nested_list = []
for list_list in FlatList(nested_list):
    for item in range(0, len(list_list)):
        not_nested_list.append(list_list[item])
print(not_nested_list)
