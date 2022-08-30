'''
 min -> 1 2 3 4 5 
 max -> 5 4 3 2 1 
 

 1 3 5 4 3 2 1
 1 4 5 3 3 2 1
 2 4 5 3 3 1 1
 3 4 5 3 2 1 1
'''


def solve(nums):
    N = len(nums)
    pivot = 0
    # find pivot
    for i in reversed(range(1,N)):
        if nums[i-1] < nums[i]:
            pivot = i
            break

    if pivot == 0:
        nums.sort()
        return 


    # the find swap s.t first number > piviot 
    swap = N - 1
    while nums[pivot-1] >= nums[swap]:
        swap -= 1
    # swap
    nums[pivot-1],nums[swap] = nums[swap],nums[pivot-1]
    # reverse from pivot
    nums[pivot:] = sorted(nums[pivot:])

def Main():
    ans = solve([1,3,2]) # [2,1,3]
    print(f"\nAnswer:{ans}\n")


if __name__ == "__main__":
    Main()