'''
    Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.

    Chech whether A has redundant braces or not.

    NOTE: A will be always a valid expression.
'''


# O(N) runtime | O(N) spacetime
def solve(A):
    stack = []
    for c in A:
        if c != ")":
            stack.append(c)
        else:
            count = 0
            while stack[-1] != "(":
                popped = stack.pop()
                if popped in "+-*/": count +=1
            stack.pop()

            if count == 0: return 1
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