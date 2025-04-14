class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # to avoid duplicates if we need to sort it so its clos to each other
        # dfs with a backtrack

        res = []
        candidates.sort()

        def dfs(i, path, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return
            if curr_sum > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                curr_sum += candidates[j]
                dfs(j + 1, path, curr_sum)
                path.pop()
                curr_sum -= candidates[j]

        dfs(0, [], 0)
        return res