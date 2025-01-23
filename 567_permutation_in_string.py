class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # basically if i have a permutation i can just throw it inside that hashmap and start dynamicaly checking it 
        a_hash = Counter(s1)
        b_hash = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] in b_hash:
                b_hash[s2[r]] += 1
            else:
                b_hash[s2[r]] = 1

            if r - l + 1 > len(s1):
                if b_hash[s2[l]] == 1:
                    del b_hash[s2[l]]
                else:
                    b_hash[s2[l]] -= 1
                l += 1

            if a_hash == b_hash:
                return True
        return False