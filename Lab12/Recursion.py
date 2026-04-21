#
# def sum_digits(x: int) -> int:
#     if x <= 9:
#         return x
#     else:
#         return x % 10 + sum_digits(x // 10)
# print(sum_digits(12345))
#
# def reverse_string(s: str) -> str:
#     if len(s) == 1:
#         return s
#     return s[-1] + reverse_string(s[:-1])
# print(reverse_string("hello"))
#
# def find_max(num_list: list[int]):
#     if len(num_list) == 1:
#         return num_list[0]
#     if num_list[0] > find_max(num_list[1:]):
#         return num_list[0]
#     else:
#         return find_max(num_list[1:])
# print(find_max([7,2,8]))
#
# def power(base, exp):
#     if exp == 0:
#         return 1

#lin_search([1,2,3], 2, 0) -> '1' because 2 is at index 1
def lin_search(vals: list[int], target: int, i: int):
    if target not in vals:
        return -1
    else:
        if vals[i] == target:
            return vals[i]
        else:
            return lin_search(vals, target, i + 1)
print(lin_search([2,4,5,9,3], 3, 0))



def bin_search(vals: list[int], target: int):
    return bin_search_h(vals,target, 0, len(vals) - 1)

def bin_search_h(vals: list[int], target: int, low: int, high: int):
    pass
    