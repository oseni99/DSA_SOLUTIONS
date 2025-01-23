class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return false
        l = 0
        r = len(s1) - 1  
        while r < len(s2):
            print(s2[l:r+1])
            if s2[l:r+1] == s1 or s2[l:r+1][::-1] == s1:
                return True
            l += 1
            r += 1
        return False