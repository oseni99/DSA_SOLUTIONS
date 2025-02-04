class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for r in tokens:
            if r not in {"+", "-", "/", "*"}:
                my_stack.append(int(r))
            else:
                a = my_stack.pop()
                b = my_stack.pop()
                if r == "+":
                    my_stack.append(a + b)
                if r == "-":
                    my_stack.append(b - a)
                if r == "*":
                    my_stack.append(b * a)
                if r == "/":
                    my_stack.append(int( b / a))
        return my_stack[0]