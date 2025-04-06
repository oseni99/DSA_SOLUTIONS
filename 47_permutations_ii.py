class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(
            nums
        )  # to know what number ive used in the recursion stack

        # its basically me just getting the whole combinations thats there
        # because it has to be unique im going to keep track of the

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                # if ive used the number before
                if used[i]:
                    continue

                # i also want to skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                dfs(path)

                path.pop()
                used[i] = False

        dfs([])
        return res