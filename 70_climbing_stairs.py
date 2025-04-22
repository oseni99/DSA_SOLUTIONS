class Solution:
    def climbStairs(self, n: int) -> int:
        # this looks like a case of backtracking or so to me
        # you can only make 2 choices at one point

        self.res = 0

        def dfs(i):
            # base case
            if i == n:
                self.res += 1
                return
            if i > n:
                return
            dfs(i + 1)
            dfs(i + 2)

        dfs(0)
        return self.res