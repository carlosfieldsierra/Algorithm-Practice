class Solution:
    # O(N) runtime | O(N) spacetime
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        index = m + n - 1
        
        m = m - 1
        n = n - 1
        
        while m != -1 and n != -1:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -=1 
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1
        
        while m != -1:
            nums1[index] = nums1[m]
            m -= 1
            index -= 1
            
        while n != -1:
            nums1[index] = nums2[n]
            n -= 1
            index -= 1
            
        return nums1