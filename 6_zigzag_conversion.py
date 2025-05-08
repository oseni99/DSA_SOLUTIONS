class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # simukate those rows to go down and up when its at the ennd
        if numRows == 1:
            return s 
        rows = [[] for _ in range(numRows)]
        d = 1
        i = 0

        for char in s:
            rows[i].append(char)
            if i == numRows - 1:
                d = -1
            elif i == 0:
                d = 1
            i += d

        res = ""
        for i in range(numRows):
            res += "".join(rows[i])

        return res