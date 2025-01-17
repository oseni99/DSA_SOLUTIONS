class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new = sorted(intervals)
        res = []
        curr = new[0]
        for i in range(1, len(new)):
            if curr[1] >= new[i][0]:
                curr = [curr[0], max(curr[1], new[i][1])]
            else:
                res.append(curr)
                curr = new[i]
        res.append(curr)
        return res