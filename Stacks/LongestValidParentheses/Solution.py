
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
# 
def solve(s):
    n = len(s)
    is_ok = [0 for _ in s]
    stack = []

    for i,c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            if stack:
                is_ok[stack.pop()] = 1
                is_ok[i] = 1

    count = 0
    ans =  0
    for i in range(len(s)):
        if is_ok[i]: count += 1
        else: count = 0
        ans = max(ans,count)
    return ans

def Main():
    ans = solve("(()")
    print(f"\nAnswer: {ans}\n")


if __name__ == "__main__":
    Main()