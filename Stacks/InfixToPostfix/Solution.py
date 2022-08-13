'''

'''

def solve(infix):
    priority = {
        "+":0,
        "-":0,
        "*":1,
        "/":1,
        "(":2,
        ")":2,
    }
    postfix = []
    stack = []

    for token in infix:
        if token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            postfix.append(")")
        elif token not in "+-/*":
            postfix.append(token) 
        else:   
            while stack and priority[stack[-1]] >= priority[token]:
                postfix.append(stack.pop())

            stack.append(token)

    while stack:
        postfix.append(stack.pop())

    return postfix


def Main():
    ans = "".join(solve("1+4/2*6-3"))
    print(f"\nAnswer: {ans}\n")
    ans = "".join(solve("(1+(4+5+2))"))
    print(f"\nAnswer: {ans}\n")

if __name__ == "__main__":
    Main()