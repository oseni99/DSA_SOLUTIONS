class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #  [1,3,5,6]
        #  whenever i cant just return that middle index plus one
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if nums[m] < target:
            return m + 1
        else:
            return 0