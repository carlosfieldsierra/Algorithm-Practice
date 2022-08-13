'''
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
'''


# O(N) runtime | O(N) spacetime
def solve(s):
    stack = [letter for letter in s]
    stack.reverse()
    ansStack = []
    while stack:
        value = stack.pop()
        if not ansStack:
            ansStack.append(value)
            continue
        
        curTop = ansStack[-1]
        if curTop == "(" and value==")":
            ansStack.pop()
        elif curTop == "{" and value=="}":
                ansStack.pop()
        elif curTop == '[' and value == ']':
            ansStack.pop()
        else:
            ansStack.append(value)
        
    return len(ansStack) ==  0


def Main():
    ans = solve("()[]{}")
    print(f"answer: {ans}")

if __name__ == "__main__":
    Main()