'''
    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

'''

# O(N) runtime | O(N) spacetime
def solve(s):
    remove = []
    stack = []
    
    for i in range(len(s)):
        c = s[i]
        if c == "(":
            stack.append(i)
        
        if c == ")":
            if stack:
                stack.pop()
            else:
                remove.append(i)
    
    remove = stack + remove
    retStr = ""
    for i in range(len(s)):
        if i not in remove:
            retStr += s[i]
            
    return retStr 

def Main():
    for A in [
        "lee(t(c)o)de)",
        "))("
    ]:
        ans = solve(A)
        print(f"answer: {ans}")

if __name__ == "__main__":
    Main()