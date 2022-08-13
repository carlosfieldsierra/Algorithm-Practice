'''
    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

'''

def solve(s):
    is_ok = [0]*len(s)
    stack = []

    for i,c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                is_ok[stack.pop()]  = 1
                is_ok[i] = 1
        
    ans = ""
    for i,c in enumerate(s):
        if c in "()":
            if is_ok[]:
                pass
def Main():
    for A in [
        "lee(t(c)o)de)",
        "))("
    ]:
        ans = solve(A)
        print(f"answer: {ans}")

if __name__ == "__main__":
    Main()