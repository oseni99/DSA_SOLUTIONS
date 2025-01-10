class Solution:
    def longestPalindrome(self, s: str) -> str:
        # i treat it like its the center
        def check_from_center(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        res = ""
        for i in range(len(s)):
            odd_path = check_from_center(i, i)
            even_path = check_from_center(i, i + 1)

            res = max(odd_path, even_path, res, key=len)
        return res