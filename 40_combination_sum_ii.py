class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # we have to use dfs with backtracking here
        #  i know that i cannot use a single number twice
        candidates.sort()
        res = []

        def dfs(idx, subsets, curr_sum):
            if curr_sum == target:
                res.append(subsets.copy())
                return
            if curr_sum > target:
                return

            # i now go through it, can add one or ignore it
            for i in range(idx, len(candidates)):
                # skip that duplicates 
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                # add that candidates
                subsets.append(candidates[i])
                # recursive
                dfs(i + 1, subsets, curr_sum + candidates[i])
                # when this is done
                subsets.pop()

        dfs(0, [], 0)
        return res