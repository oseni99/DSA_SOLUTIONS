class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i pick one number and i do the BS on it to see if it matches
        res = []
        #  i have to also sort it for BS to work
        # i have to skip it also if the current number is the same as the previous
        # because we will have the same answer again which is duplictes
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  #  skip it
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # there might be multiple results using that same i
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                if target > 0:
                    r -= 1
                if target < 0:
                    l += 1
        return res