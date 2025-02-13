class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = 0
        r = 1
        stack = [0] * len(temperatures)
        while r < len(temperatures):
            if temperatures[l] < temperatures[r]:
                stack[l] = r - l
                r = l + 1
                l += 1
            else:
                r += 1
        return stack