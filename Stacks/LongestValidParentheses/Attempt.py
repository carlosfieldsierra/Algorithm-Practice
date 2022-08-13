
'''
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

    Example 1:

    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".
    Example 2:

    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".
    Example 3:

    Input: s = ""
    Output: 0

'''
# O(N^3) runtime | O(N) spacetime  
def solve(s):
    
    count = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            print(s[i:j+1])
            if isValid(s[i:j+1]):
                count = max(count,len(s[i:j+1]))
    
    return count
    
    

def isValid(s):
    remove = []
    stack = []
    for i in range(len(s)):
        c = s[i]
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                remove.append(i)
    
    remove = stack + remove
    
    return len(remove) == 0
    

def Main():
    ans = solve("(()")
    print(f"answer: {ans}")


if __name__ == "__main__":
    Main()