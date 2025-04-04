class Solution:
    def fib(self, n: int) -> int:
        # just used dp bottm to top
        dp = [0, 1]
        if n < 2:
            return n
        i = 2
        while i <= n:
            dp[1], dp[0] = dp[1] + dp[0], dp[1]
            i += 1
        return dp[1]