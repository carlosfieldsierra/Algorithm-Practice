class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        stack = []
        for i in range(N):
            newIndex = (i + k) % N
            stack.append((nums[i],newIndex))
            nums[i] = 0
            
        while stack:
            val,index = stack.pop()
            nums[index] = val
            
            
        
            
        
        