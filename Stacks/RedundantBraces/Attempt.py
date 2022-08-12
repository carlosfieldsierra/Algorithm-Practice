'''
    Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.

    Chech whether A has redundant braces or not.

    NOTE: A will be always a valid expression.
'''


# O(N) runtime | O(N) spacetime
def solve(A):
    stack = []
    ops = "+-*/"
    for c in A:
        if c == "(":
            stack.append(c)
        if c in ops:
            if stack and stack[-1] == "(":
                stack.append(c)
        if c == ")":
            if stack[-1] not in ops:
                return 1
            stack.pop()
            stack.pop()
    return 0

def Main():
    for a in [
            "((a+b))",
            "(a+(a+b))"
        ]:
        ans = solve(a)
        print(f"answer: {ans}")

if __name__ == "__main__":
    Main()