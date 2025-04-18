class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # whats happening is that at each point im making the number if its a character a capital letter and when im at the end i just pop back and try the other

        res = []

        def dfs(i, path):
            # base case
            if len(path) == len(s):
                res.append(path)

            for j in range(i, len(s)):
                # so basically im just checking if its an alphabet so i try both the upper and lower
                if s[j].isalpha():
                    dfs(j + 1, path + s[j].upper())
                    dfs(j + 1, path + s[j].lower())
                else:
                    dfs(j + 1, path + s[j])

        dfs(0, "")
        return res