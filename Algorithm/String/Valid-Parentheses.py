"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

def validParentheses(s):
    valid_dict = {'(': ')', '{':'}', '[': ']'}
    s_stack = list()
    for c in s:
        if c in valid_dict:
            s_stack.append(valid_dict[c])
        else:
            if s_stack:
                if c != s_stack.pop():
                    return False
            else:
                return False
    if s_stack:
        return False
    return True

print(validParentheses("()[]{}"))
print(validParentheses("([)]"))
print(validParentheses("]"))
