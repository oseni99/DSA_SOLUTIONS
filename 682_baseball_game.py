class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i not in {"D", "+", "C"}:
                stack.append(int(i))
            else:
                if i == "+":
                    stack.append(stack[-1] + stack[-2])
                if i == "D":
                    stack.append(stack[-1] * 2)
                if i == "C":
                    stack.pop()
        return sum(stack)