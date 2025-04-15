class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        # i just have to check if ive used that index where that number is
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return res