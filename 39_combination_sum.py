class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, subsets, curr_sum):
            if curr_sum == target:
                res.append(subsets.copy())
                return

            if curr_sum > target:
                return

            for i in range(idx, len(candidates)):
                # i want to add it
                subsets.append(candidates[i])
                # because i can use it again i dont have to increase the i
                dfs(i, subsets, curr_sum + candidates[i])
                # i also want to backtrack if im done
                subsets.pop()

        dfs(0, [], 0)
        return res