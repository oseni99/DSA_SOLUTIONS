class Solution:
    def climbStairs(self, n: int) -> int:
        # backtracking with recursion will TLE
        # dp with memoization/bottom down dp

        if n <= 1:
            return 1
        dp = [1, 1]

        # we just need the two previous
        for _ in range(2, n + 1):
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
        return dp[1]