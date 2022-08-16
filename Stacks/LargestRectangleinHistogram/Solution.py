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

'''
    heights = [1,3,2,5,4,1,3]
    ex)

          #
          # #
      #   # #   #
      # # # #   #
    # # # # # # #
    -------------
    0 1 2 3 4 5 6


         #
         #  # 
    [ #, #, # ]

    ==================

    right_span = r - i - 1 
    left_span  = i - l - 1
    width = left_span + right_span + 1

    r = 4
    l = 2
    right_span = 5 - 4 - 1 
                = 0 
    left_span  = 4 - 2 - 1 
                = 1

    width = 1 + 0 + 1
            = 2
'''
def visualize(array,l,ii,r):
    maxHeight = max(array)

    matrix = [[" " for _ in range(len(array))] for _ in range(maxHeight)]

    for i in range(len(array)):
        elem = array[i]
        for j in range(elem):
            matrix[maxHeight-j-1][i] ="x"
    
    end = [" " for _ in range(len(array))]
    end[l] = "l"
    end[ii] = "i"
    end[r] = 'r'
    matrix.append(end)
    for row in matrix:
        print(*row)
    print("\n\n")

# O(N) runtime | O(N) spactime
def solve(heights):
    n = len(heights)  
    heights.append(0) # hacky solution
    stack = []
    ans = 0
 
    for r in range(n):
        while stack and heights[r] <= heights[stack[-1]]:
            i =  stack.pop()
            l = stack[-1] if stack else -1

            right_span = r - i - 1
            left_span  = i - l - 1
            
            width = left_span + right_span + 1
            area  = heights[i] * width
            ans   =  max(ans,area)
        
        stack.append(r)
    

    return ans

 
def Main(): 
    ans = solve([1,3,2,5,4,1,3])
    print(f"\nAnswer:{ans}\n")
    ans = solve([2,1,5,6,2,3])
    print(f"\nAnswer:{ans}\n")

 
if __name__ == "__main__":
    Main() 