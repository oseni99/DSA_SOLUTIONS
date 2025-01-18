from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # I CAN ONLY SWAP ONE RIGHT
        #  I THINK I CAN USE TWO POINTERS AND DO IT LIKE THIS
        if len(s) != len(goal):
            return False
        if len(s) == 2:
            return s[::-1] == goal
        if s == goal:
            s_hash = Counter(s)
            goal_hash = Counter(goal)
            for i, j in s_hash.items():
                if s_hash[i] >= 2:
                    return True
            return False
        l = 0
        r = 0
        new_s = list(s)
        new_goal = list(goal)
        while l < len(new_s) or r < len(new_goal):
            if new_s[l] != new_goal[r]:
                # find the index of that goal
                idx = s.find(goal[r],l+1)
                new_s[l], new_s[idx] = new_s[idx], new_s[l]
                return new_s == new_goal
            else:
                l += 1
                r += 1
        return False