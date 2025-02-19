class Solution:
    def findMin(self, nums: List[int]) -> int:
        #  can use binary search
        # its two things
        # i have to check my middle with the right most part
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                #  if its greater thna the right most it will always be at the right
                l = m + 1
            else:
                r = m
        return nums[l]