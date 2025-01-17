class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        curr_end = 0
        for i in timeSeries:
            if i > curr_end:
                res += duration 
            else:
                res += (i + duration - curr_end)
            curr_end = i + duration 
        return res