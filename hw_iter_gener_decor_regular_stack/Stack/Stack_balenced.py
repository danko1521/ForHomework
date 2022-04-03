open_list = ["[", "{", "("]

close_list = ["]", "}", ")"]


def check(element):
    stack = []
    for i in element:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and open_list[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return f"Unbalanced"
    if len(stack) == 0:
        return f"Balanced"


string1 = '{[{()}}'
ans = check(string1)
print(ans)