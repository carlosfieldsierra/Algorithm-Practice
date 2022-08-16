'''
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

    

    Example 1:


    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
    Example 2:

    Input: height = [4,2,0,3,2,5]
    Output: 9
    

    Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
'''

def solve2(height):
    n = len(height)
    maxLeft = [0] * n
    maxRight = [0] * n
    
    for i in range(1,n):
        maxLeft[i] = max(maxLeft[i-1],height[i-1])
        
        index = n - 1 - i
        maxRight[index] = max(maxRight[index+1],height[index+1])
        
    
    ans = 0
    for i in range(n):
        waterLevel = min(maxLeft[i],maxRight[i])
        if waterLevel >= height[i]:
            ans += waterLevel - height[i]
    
    return ans


def solve(height):
    total = 0
    stack = []
    for r in range(len(height)):
        while stack and height[r] >= height[stack[-1]]:
            m   = stack.pop()
            
            if not stack: break

            width = r - stack[-1] - 1
            minHeight = min(height[r],height[stack[-1]])

            left_height = minHeight - height[m]

            total += width * left_height

        stack.append(r) 
    
    return total




def Main():
    ans = solve([4,2,0,3,2,5]) # 9
    print(f"\nAnswer: {ans}\n")
    ans = solve([0,1,0,2,1,0,1,3,2,1,2,1]) # 6
    print(f"\nAnswer: {ans}\n")

if __name__ == "__main__":
    Main()