'''
    907. Sum of Subarray Minimums
    Medium

    4012

    265

    Add to List

    Share
    Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

    

    Example 1:

    Input: arr = [3,1,2,4]
    Output: 17
    Explanation: 
    Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
    Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
    Sum is 17.
    Example 2:

    Input: arr = [11,81,94,43,3]
    Output: 444
    

    Constraints:

    1 <= arr.length <= 3 * 104
    1 <= arr[i] <= 3 * 104
'''

from inspect import stack


def visualize(arr,i,j,result,stack):
    memo = [" "]*len(arr)
    memo[i] = "i"
    memo[j] = "j"
    
    print("--"*len(arr))
    print(*arr)
    print(*memo)
    print("--"*len(arr))
    
    print(*arr)
    print(*memo)
    print("--"*len(arr)*2)
    print("Stack:", stack)
    print("--"*len(arr)*2)
    print("Result: ",*result)
    print("--"*len(arr)*2)
    print("\n\n")
    

def solve2(A):
    A = [0]+A
    result = [0]*len(A)
    stack = [0]
    for i in range(len(A)):
        print( A[stack[-1]] ,">", A[i])
        while A[stack[-1]] > A[i]:
            print( A[stack[-1]] ,">", A[i])
            print(f"stack: {[A[m] for m in stack]}")
            stack.pop() 
            print(f"stack: {[A[m] for m in stack]}")
        j = stack[-1]
        print(f"stack: {[A[m] for m in stack]} and i is {i} and {j} so i-j is {i-j} so i-j *A[i] is {(i-j)*A[i]} and res[j] is {result[j]}" )
        result[i] = result[j] + (i-j)*A[i]
        print(f"result[i]: {result[i]}")
        stack.append(i)
        # Vis
        # visualize(A,i,j,result,stack)
    return sum(result) % (10**9+7)

# O(N) runtime | O(1) spactime
def solve(arr):
    arr.append(-float("inf"))
    n = len(arr)
    stack = [] 
    ans = 0
    for r in range(n):
        while stack and arr[r] <=arr[stack[-1]]:
            i = stack.pop()
            l = stack[-1] if stack else -1 

            left_span = i - l
            right_span = r - i

            count = left_span * right_span
            ans += arr[i] * count
        
        stack.append(r)

    return ans



def Main():
    ans = solve2([1,2,3]) # 17
    print(f"\nAnswer: {ans}\n")


if __name__ == "__main__":
    Main()
