class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #  i know i can either do two things --> either i add one or ignore one and it continues recursively

        res = []
        subset = []

        def dfs(i):
            #  base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # i want to include the next num
            subset.append(nums[i])
            dfs(i + 1)

            # i want to not include it
            subset.pop()  # i backtrack
            dfs(i + 1)

        dfs(0)
        return res