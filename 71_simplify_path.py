class Solution:
    def simplifyPath(self, path: str) -> str:
        res = path.split("/")
        stack = []
        ans = []
        for i in res:
            if i == "...":
                stack.append("...")
            elif i == "..":
                stack.pop()
            elif i == "":
                stack.append("/")
            elif i == ".":
                continue
            else:
                stack.append(i)
        print(stack)
        while len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        for i in range(len(stack)):
            if stack[i] != "/" and i < len(stack) - 1:
                a = stack[i] + "/"
                ans.append(a)
            else:
                ans.append(stack[i])
        print(ans)
        return "".join(ans)