class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        # Reverse
        l,r = 0, N -1
        while r > l:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        
        l, r = 0, k - 1
        while r > l:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1


        l, r = k, N - 1
        while r > l:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        
            
        

        