class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(cp):
            curr = 0
            res = 1
            for i in weights:
                if curr + i > cp:
                    res += 1
                    curr = 0
                curr += i
            return res

        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (l + r) // 2
            if helper(m) <= days:
                r = m
            else:
                l = m + 1
        return l