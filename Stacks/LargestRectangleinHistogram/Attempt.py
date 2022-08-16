'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
 
Input: heights = [2,4]
Output: 4
'''

# Failed Attempt
def solve(heights):
    n = len(heights)
    stack = []
    maxArea = 0
    
    
    for r in range(n):
        while stack and heights[r] < heights[stack[-1]]:
            end = stack.pop()
            if not stack: break
            
            start = stack[-1]
            
            width = end - start + 1 
            
            area = width * min(heights[start],heights[end])
            maxArea = max(area,maxArea)
        stack.append(r)

    # Stack left 
    
    start,end = stack[0],stack[-1]
    width = end - start + 1
    area = width * heights[stack[0]]
    maxArea = max(maxArea,area)


    return maxArea
    



def Main():
    ans = solve([2,1,5,6,2,3])
    print(f"\nAnswer:{ans}\n")
    ans = solve([2,4])
    print(f"\nAnswer:{ans}\n")


if __name__ == "__main__":
    Main()