# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def isValid( s):
    """
    :type s: str
    :rtype: bool
    """
    parentheses = { #hashmap for matching parentheses
    ')': '(',
    '}': '{',
    ']': '['
    }
    stack = []
    for p in s:
        if p in parentheses: #if p is a closing bracket and the stack is empty,or if top character of stack != corresponding opening bracket of p, then string is not valid.
            if stack and stack[-1] == parentheses[p]:
                stack.pop()
            else:
                return False
        else:
            stack.append(p)
    return True if not stack else False  #return true if stack is empty and all brackets have been taken care of; else return false

print(isValid("))"))
        