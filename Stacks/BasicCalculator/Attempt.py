'''
    Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

    

    Example 1:

    Input: s = "1 + 1"
    Output: 2
    Example 2:

    Input: s = " 2-1 + 2 "
    Output: 3
    Example 3:

    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23
    

    Constraints:

    1 <= s.length <= 3 * 105
    s consists of digits, '+', '-', '(', ')', and ' '.
    s represents a valid expression.
    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.
'''



operators = "()/*+-"
priority = {
    "(":-1,
    "/":1,
    "*":1,
    "+":0,
    "-":0,
}

def solve(s):
    infix = read(s)
    print(infix)

def read(s):
    infix = []

    i = 0
    while i < len(s):
        if s[i] == "":
            i += 1
        elif s[i] in "()/*+-":
            if s[i]=="-":
                if i == 0 or i-1>=0 and  s[i-1]== "(":
                    infix.append(0)
            infix.append(s[i])
            i += 1
        else:
            number = ""
            while i < len(s) and s[i].isdigit():
                number += s[i]
                i += 1 
            infix.append(number)
    return infix 

def infix_to_postfix(infix):
    pass

def evalulate_postfix(postfix):
    pass

def Main():
    ans = solve("(1+(4+5+2)-3)+(6+8)")
    print(f"\nAnswer: {ans}\n")

if __name__ == "__main__":
    Main()