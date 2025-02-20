class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max it can be is the max number in the piles
        # min is the minimum number it can be to eat that pile which is one
        l = 1
        r = max(piles)
        while l <= r:
            m = l + (r - l) // 2
            curr = 0
            for i in piles:
                curr += math.ceil(i / m)
            if curr <= h:
                r = m - 1
            else:
                l = m + 1
        return l