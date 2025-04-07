class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if i pick any number i have to find the hashmap and combine every letter
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

        def dfs(idx, curr_str):
            # base case
            if len(digits) == len(curr_str):
                res.append(curr_str)
                return
            letters = store[digits[idx]]
            for i in letters:
                dfs(idx + 1, curr_str + i)

        dfs(0, "")
        return res