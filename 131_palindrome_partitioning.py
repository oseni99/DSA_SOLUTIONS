class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # i try each of those substrings and i check if its still substring palindrome
        # thats when i still even continue to check it

        res = []
        subs = []

        def is_palindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            # base case
            if i >= len(s):
                res.append(subs.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    subs.append(s[i : j + 1])
                    dfs(j + 1)
                    subs.pop()

        dfs(0)
        return res