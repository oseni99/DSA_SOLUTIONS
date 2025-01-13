class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ""
        i = 0
        while len(res) < len(s) and i < len(words):
            res += words[i]
            print(res)
            i += 1
        return res == s