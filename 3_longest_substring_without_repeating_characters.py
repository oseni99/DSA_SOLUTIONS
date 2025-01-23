class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = set()
        maxLen = 0
        while r < len(s):
            if s[r] not in res:
                res.add(s[r])
                r += 1
                maxLen = max(maxLen, r - l)
            else:
                res.remove(s[l])
                l += 1
        return maxLen