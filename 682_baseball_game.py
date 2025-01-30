class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        records = {
            "+": 1,
            "D": 2,
            "C": 3,
        }
        stack = []
        for i in operations:
            if i not in records.keys():
                res += int(i)
                stack.append(int(i))
                print(stack)
            else:
                if i == "+":
                    curr = stack[-1] + stack[-2]
                    res += curr
                    stack.append(curr)
                if i == "D":
                    curr = stack[-1] * 2
                    res += curr
                    stack.append(curr)
                if i == "C":
                    curr = stack.pop()
                    res -= curr
        return res