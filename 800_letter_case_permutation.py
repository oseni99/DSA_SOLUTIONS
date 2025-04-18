class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # whats happening is that at each point im making the number if its a character a capital letter and when im at the end i just pop back and try the other

        res = []

        def dfs(i, path, used):
            # base case
            if len(path) == len(s):
                if path not in used:
                    res.append(path)
                    used.add(path)

            for j in range(i, len(s)):
                letter = s[j]
                if letter.isalpha():
                    new = letter.upper()
                    dfs(j + 1, path + new, used)
                dfs(j + 1, path + letter, used)

        dfs(0, "", set())
        return res