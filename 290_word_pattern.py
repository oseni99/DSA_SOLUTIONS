class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # two hashmaps to keep track of that word and its pattern 
        s_hash = {}
        p_hash = {}
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        # i use zip to group them together 
        for p, c in zip(pattern, words):
            if p not in p_hash:
                if c in s_hash:
                    return False
                else:
                    p_hash[p] = c
                    s_hash[c] = p
            else:
                if p_hash[p] != c:
                    return False
        return True