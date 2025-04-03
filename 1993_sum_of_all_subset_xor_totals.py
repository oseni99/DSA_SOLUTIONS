class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # subarray is diff from subset and the XOR is just dealing with binary
        # we keep a track of all the total and its 2 to the power of n

        def dfs(i, total):
            # base case
            if i == len(nums):
                return total
            #  two things can happen
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)

        return dfs(0, 0)