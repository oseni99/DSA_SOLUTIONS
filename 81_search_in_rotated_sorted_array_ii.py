class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            if nums[l] < nums[m]:  # left portion
                if nums[l] <= target < nums[m]:  # checking if its in left sorted part
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:  # right portion
                if ( nums[m] < target <= nums[r]):  # checking if target is in right sorted part
                    l = m + 1
                else:
                    r = m - 1
            else:  # if its equal i just want to shrink it and move l by 1
                l += 1
        return False