class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # its a backtracking with dfs
        res = []
        sub_parts = []

        def is_palindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(idx):
            # base case when the index is at the end
            if idx >= len(s):
                res.append(sub_parts.copy())
                return

            for i in range(idx, len(s)):
                if is_palindrome(s, idx, i):
                    sub_parts.append(s[idx : i + 1])
                    dfs(i + 1)
                    sub_parts.pop()

        dfs(0)
        return res