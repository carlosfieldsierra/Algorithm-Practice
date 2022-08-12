'''
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
'''
def solve(s):
    mapping = {
        "}":"{",
        ")":"(",
        "]":"["
    }
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if stack:
                
                if mapping[c] == stack[-1]:
                    stack.pop() 
                else:
                    return False  
                   
    return len(stack) == 0

def Main():
    ans = solve("()[]{}")
    print(f"answer: {ans}")

if __name__ == "__main__":
    Main()