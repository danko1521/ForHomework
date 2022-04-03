import os
import functools
from datetime import datetime

nested_list = [
    ['a', 'b', 'c'], [1, 2, 3, 4, 5, 6, 7, 8], ['d', 'e', 'f', 'h', False], ['d', 'e', 'f', 'h', False], [1, 2, None]
]


def param_decor(param):
    def actual_debug_decor(func):
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            print(f'находится в дериктории - {param}')
            print(f"вызывается функция {func.__name__} с аргументом({signature})")
            value = func(*args, **kwargs)
            print(f"функция {func.__name__!r} вернула аргумент {value!r}")
            now = datetime.now()
            current_time = now.strftime("%y:%m:%d:%H:%M:%S")
            with open("loger.txt", "w") as file:
                file.write(f'time calling function {current_time}, name func {func.__name__},'
                           f' func return argument {signature} and return value {value}')
            return value

        return wrapper_debug

    return actual_debug_decor


@param_decor(param=os.path)
class flat_list:

    def __init__(self):
        self.list = nested_list
        self.flat_list = []

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        flat_list = []

        for element in nested_list:
            if type(element) is list:

                for item in element:
                    flat_list.append(item)
            else:
                flat_list.append(element)
        return flat_list


List_iter = flat_list()
for reading in List_iter:
    print(reading)
    break
