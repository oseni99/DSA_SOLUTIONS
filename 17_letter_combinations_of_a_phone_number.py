class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        if not digits:
            return []

        def dfs(i, path):
            # base case
            if len(path) == len(digits):
                res.append(path)
                return
            letters = store[digits[i]]
            for j in letters:
                dfs(i + 1, path + j)

        dfs(0, "")
        return res