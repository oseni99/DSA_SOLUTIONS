class Solution:
    def simplifyPath(self, path: str) -> str:
        res = path.split("/")
        stack = []
        for i in res:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == "":
                continue
            else:
                stack.append(i)
        return "/" + "/".join(stack)