from typing import TypeVar

list_of_strings: list[TypeVar] = ["hello", "Hello", "Hola", "Salut"]
list_of_ints: list[TypeVar] = [1, 2, 2, 4, 5, 5, 5, 9]
list_of_floats: list[TypeVar] = [2.5, 2.5, 2.5, 3.7, 8.5, 9.2, 9.2]
list_of_bad_stuff: list[TypeVar] = [1, "Hello", 2.5]

def occurences(list_inputed: list[TypeVar]) -> dict[TypeVar, int]:
    count_dict: dict[TypeVar, int] = {}
    count: int = 1

    for i in list_inputed:
        if i in count_dict:
            count_dict[i] += count
        else:
            count_dict[i] = count
    return count_dict

if __name__ == '__main__':
    print(occurences(list_of_ints))