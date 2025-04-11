class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # we know that a square has 4 sides and each are all symmetrical
        # we have to divide the sum of the length by 4 first to get the sides
        # it has to be an integer and not a float
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        length = total // 4
        sides = [0] * 4  # building the sides of the square
        matchsticks.sort(
            reverse=True
        )  # if the biggest is less than length then it wont work

        def backtrack(i):
            # basecasee
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False

        return backtrack(0)