class Solution:
    def threeSum(self, nums):
       res = []
       nums.sort()
       
       for i, a in enumerate(nums):
        if i > 0 and a == nums[i -1]:
            continue

        l, r = i +1 , len(nums) - 1
        while r > l:
            threeSum = a + nums[l] + nums[r]
            if threeSum == 0:
                res.append([a,nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and r > l:
                    l += 1
            elif threeSum > 0:
                r -= 1
            else:
                l += 1
            

       return res

        






def Main():
    ans = Solution().threeSum([-3,3,4,-3,1,2])
    print(f"\nAnswer: {ans}\n")


if __name__ == "__main__":
    Main()