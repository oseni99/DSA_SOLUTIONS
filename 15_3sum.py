class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicate numbers for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1  # Two pointers, left and right

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Skip duplicates for r
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res