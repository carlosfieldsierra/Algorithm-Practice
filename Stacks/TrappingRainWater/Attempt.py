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


# Failed Attempt 

def solve(height):
    if height==[]:
        return 0
    waterArea = 0
    # Peak to Larger Peak
    stack = [0]
    for bar in range(1,len(height)):
        # 
        stack.append(bar)
        
        if height[bar] >= height[stack[0]]:
            subWaterArea = 0
            startIndex,*midIndexes,endIndex = stack 
            start = height[startIndex]
            mid   = [height[index] for index in midIndexes]
            end   = height[endIndex]
            for elem in mid:
                subWaterArea += start - elem
            waterArea += subWaterArea
            stack = [endIndex]
            

    print(waterArea,height[stack[0]+1:len(height)])
    # Peak to Drop off 
    waterArea += solve(height[stack[0]+1:len(height)])
        
    
    return waterArea

def Main():
    ans = solve([0,1,0,2,1,0,1,3,2,1,2,1])
    print(f"\nAnswer: {ans}\n")

if __name__ == "__main__":
    Main()