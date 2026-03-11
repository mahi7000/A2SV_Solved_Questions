class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            f = False
            if c == ")":
                num = 0
                while stack and stack[-1] != '(':
                    y = stack.pop()
                    num += y
                    f = True
                stack.pop()
                if f:
                    stack.append(2 * num)
                else:
                    stack.append(1)

            else:
                stack.append(c)

        return sum(stack)