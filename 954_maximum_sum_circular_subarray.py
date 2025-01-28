class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # let me keep track of the global min and also global max
        #  im doing this because there can be negative values in it i.e kadane algo
        # the thing with the circukar part is i have to think if its all negative
        # i now have to make it the global max but if not all negative i make it
        # the max of glob_max or that total_sum - glob_min
        glob_max = nums[0]
        glob_min = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]
        total_sum = nums[0]
        for r in range(1, len(nums)):
            curr_max = max(nums[r] + curr_max, nums[r])
            curr_min = min(nums[r] + curr_min, nums[r])
            glob_max = max(glob_max, curr_max)
            glob_min = min(glob_min, curr_min)
            total_sum += nums[r]
        if glob_max < 0:
            return glob_max
        return max(glob_max, total_sum - glob_min)