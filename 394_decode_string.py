class Solution:
    def decodeString(self, s: str) -> str:
        # i have to create my stack
        #  in there i add everything unless the ]
        stack = []
        for i in s:
            if i == "]":
                curr = []
                while stack and stack[-1] != "[":
                    curr.append(stack.pop())
                stack.pop()

                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                    # the fact that we are popping from the back means we haave to reverse it
                curr.reverse()
                num.reverse()
                num_str = "".join(num)
                new_num = int(num_str)
                stack.append("".join(curr) * new_num)
            else:
                stack.append(i)
        return "".join(stack)