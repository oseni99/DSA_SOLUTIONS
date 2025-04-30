class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # first of all i know that a square has 4 equal sides
        # if its sum isnt divisible by 4 it cant ever turn the matchsticks

        total_sticks = sum(matchsticks)
        if total_sticks % 4 != 0:
            return False

        # moving to the next
        # i know that each side has to be at least total matchsticks // 4

        sticks = total_sticks // 4
        # it can also only be 4 so top bottom right left
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= sticks:
                    # move on also
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False

        return backtrack(0)