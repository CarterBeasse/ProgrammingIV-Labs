from StackPractice import StackClass

def is_balanced(expression):
    matching_dict: dict[str,str] = { ")": "(", "]": "[", "}": "{"}

    stack: list[str] = StackClass(100)

    for bracket in expression:
        # Push opening bracket onto stack
        if bracket in matching_dict.values():
            stack.push(bracket)
        elif bracket in matching_dict.keys():
            if stack.empty():
                return False
            if stack.top() != matching_dict[bracket]:
                return False
            stack.pop()
    return stack.empty()


    # Examples
expr1 = "{[()]}"
expr2 = "([)]"
expr3 = "{[]"


print(is_balanced(expr1)) # True
print(is_balanced(expr2)) # False
print(is_balanced(expr3)) # False


# for bracket in expression:
    #     # if it's an opening bracket push it onto the stack!!
    #     if bracket in matching_dict.values():
    #         stack.push(bracket)
    #     # if its closing bracket ->
    #     elif bracket in matching_dict:
    #         # if the stack is empty or the top doesn't match opening bracket
    #         if stack.empty():
    #             return False
    #         # otherwise pop the matching opening bracket from the stack
    #         if stack.top() != matching_dict[bracket]:
    #             return False
    #         stack.pop()
    # # Balanced if and only if the stack is empty at the end
    # return stack.empty()