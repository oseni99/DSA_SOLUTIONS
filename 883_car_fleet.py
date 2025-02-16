class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #  zip everything together initially
        #  reverse it so you start from the highest
        res = sorted(list(zip(position, speed)))
        stack = []
        for i in res[::-1]:
            a = (target - i[0]) / i[1]
            stack.append(a)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)