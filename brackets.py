
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
string is valid. An input string is valid if –
• Open brackets must be closed by the same type of brackets.
• Open brackets must be closed in the correct order.
'''

def balanced_brackets(s):
    s = list(s)
    brackets = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif i not in brackets.keys():
            stack.append(i)
        elif brackets[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
        
    return True if len(stack) == 0 else False

s = input()
result = balanced_brackets(s)
print(result)
