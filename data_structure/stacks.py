"""
- using pop() to get the last item (LIFO)
- pop() remove the last element

# Different between list and deque (in terms of memory allocation)
"""

# x = ["Jack", "Masha", "Kenny", "Sonya"]
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# DEQUE
from collections import deque

# stack = deque()
# stack.append("Jacky")
# stack.append("Kante")
# stack.append("Paulo")
# print(stack)
# stack.pop()
# print(stack)

# EXERSICE 1

exs_string = "We will conquere COVID19"


def reverse_string(to_reverse: str):
    stack = deque()

    for alph in to_reverse:
        stack.append(alph)

    new_stack = deque()
    for _ in range(len(stack)):
        last_word = stack.pop()
        new_stack.append(last_word)

    reverse_ = "".join(new_stack)

    return reverse_


# print(reverse_string(exs_string))

# EXERSICE 2


def is_balance(word_w_parenthesis: str):
    stack = deque()
    for alph in word_w_parenthesis:
        stack.append(alph)

    right_p = deque()
    left_p = deque()

    for elem in stack:
        if elem == "(" or elem == "[" or elem == "{":
            right_p.append(elem)
        elif elem == ")" or elem == "]" or elem == "}":
            left_p.append(elem)

    if len(right_p) == len(left_p):
        return "Balance"
    else:
        return "Unbalance"


print(is_balance("(a+b)"))
print(is_balance("(a+b"))
print(is_balance("))((a+b}{"))
