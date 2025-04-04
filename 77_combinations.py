class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #  i know that im picking from 1 to n
        #  i should make it such that when its less than n i break
        res = []

        def dfs(idx, path):
            # basecase
            if len(path) == k:
                res.append(path.copy())
                return

            for i in range(idx, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()

        dfs(1, [])
        return res