class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(s)
        new_words = "".join(words)
        if new_words[0:n] == s:
            return True
        return False