class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # throw s1 first into a hashmap
        first = Counter(s1)
        second = {}
        n = len(s1)
        l = 0
        for r in range(len(s2)):
            if s2[r] in second:
                second[s2[r]] += 1
            else:
                second[s2[r]] = 1

            if r - l + 1 == n:
                if first == second:
                    return True
                else:
                    if second[s2[l]] == 1:
                        del second[s2[l]]
                    else:
                        second[s2[l]] -= 1
                l += 1
        return False