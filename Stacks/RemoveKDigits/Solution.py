'''
    Remove K Digits

    Share
    Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

    Example 1:

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
    Example 2:

    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
    Example 3:

    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.
    

    Constraints:

    1 <= k <= num.length <= 105
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.
'''

# O(N) runtime | O(1) spacetime
def solve(num,k):
    stack = []
    for c in num:
        while k > 0 and stack and int(stack[-1]) > int(c):
            k -= 1
            stack.pop() 
        stack.append(c)

    stack = stack[:len(stack) - k]
    res = "".join(stack)

    return str(int(res))  if res else "0"

def Main():
    ans = solve(num = "10200", k = 1) # "200"
    print(f"\nAnswer: {ans}\n")


if __name__ == "__main__":
    Main()