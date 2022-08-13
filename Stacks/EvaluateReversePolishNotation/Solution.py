'''
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

    Note that division between two integers should truncate toward zero.
    It is guaranteed that the given RPN expression is always valid. That means the expression would always
    evaluate to a result, and there will not be any division by zero operation.
'''
def eval(op,a,b):
    if op  == "+":
        return a+b
    if op == "-":
        return a - b
    if op == "/":
        return a/b
    # *
    return a * b

def solve(tokens):
    stack = []

    for token in tokens:
        if token not in "+-/*":
            stack.append(int(token))
        else:
            n1 = stack.pop()
            n2 = stack.pop()
            res = eval(token,n1,n2)
            stack.append(int(res))

    return stack[0] 


def Main():
    ans = solve(["2","1","+","3","*"]) #  ((2 + 1) * 3) = 9
    print(f"\nAnswer:{ans}\n")
    ans = solve(["1","2","4","/","6","*","+","3","-"]) #  ((2 + 1) * 3) = 9
    print(f"\nAnswer:{ans}\n")  
    # ans = solve(["1","(","4","(","+","5","+","2","+",")",")"]) #  ((2 + 1) * 3) = 9
    # print(f"\nAnswer:{ans}\n")  

if __name__ == "__main__":
    Main()