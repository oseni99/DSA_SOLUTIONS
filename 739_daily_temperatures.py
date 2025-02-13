class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # anytime i see like a next greater or next less
        # i should think of a monotonic stack
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res