class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            m = (l + r) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
        # because its always comimg to the left and next greater for that nuber will always be that r
        return r