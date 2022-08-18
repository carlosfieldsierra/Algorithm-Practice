'''
    739. Daily Temperatures
    Medium

    Share
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

    

    Example 1:

    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    Example 2:

    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]
    Example 3:

    Input: temperatures = [30,60,90]
    Output: [1,1,0]
    

    Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100
'''

# O(N) runtime | O(N) spacetime
def solve(temperatures):
    n = len(temperatures)
        
    res = [0] * n
    stack = []
    
    for i in range(n):
        index = n - 1 - i
        while stack and temperatures[index] >= temperatures[stack[-1]]:
            stack.pop() 
        
        if stack:
            largerTempIndex = stack[-1]
            res[index] = largerTempIndex - index
        else:
            res[index] = 0
        
        stack.append(index)
        
    return res


def Main():
    ans = solve([73,74,75,71,69,72,76,73]) # [1,1,4,2,1,1,0,0]
    print(f"\nAnwser: {ans}\n")

if __name__ == "__main__":
    Main()