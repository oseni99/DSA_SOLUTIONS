class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # im using a number multiple times also to check
        # dfs with backtracking

        def dfs(i, path, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return
            if curr_sum > target:
                return

            for j in range(i, len(candidates)):
                path.append(candidates[j])
                curr_sum += candidates[j]
                dfs(j, path, curr_sum)
                path.pop()
                curr_sum -= candidates[j]

        dfs(0, [], 0)
        return res