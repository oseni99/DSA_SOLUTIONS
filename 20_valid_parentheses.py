class Solution:
    def isValid(self, s: str) -> bool:
        # two things to note that----> use stacks and when empty/not
        # whenever i see closing tags it has to be open for last elemtn in stack
        hash_map = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in s:
            if i in hash_map.keys():
                stack.append(i)
            elif len(stack) == 0:
                return False 
            else:
                if hash_map[stack.pop()] != i:
                    return False 
        return len(stack) == 0