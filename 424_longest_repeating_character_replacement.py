class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        l = 0
        longest = 0
        for r in range(len(s)):
            store[s[r]] = store.get(s[r], 0) + 1
            # now get the way to know if i can change all the letters to the max char under limit
            if r - l + 1 - max(store.values()) > k:
                store[s[l]] -= 1 
                l += 1
            longest = max(longest, (r - l + 1))
        return longest