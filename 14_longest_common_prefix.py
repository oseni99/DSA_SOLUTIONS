class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # basically i keep checkuing if a particular sting is the same as the shortest
        # if at any points its not equal i just return the res i have to that point
        min_str = min(strs, key=len)
        res = ""
        for i in range(len(min_str)):
            for j in strs:
                if j[i] != min_str[i]:
                    return res
            res += min_str[i]
        return res