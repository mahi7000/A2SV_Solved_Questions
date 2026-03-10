class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        s = s[::-1]
        i = 0
        while i < len(s):
            c = s[i]
            if c == '[':
                new_s = []
                while stack[-1] != ']':
                    x = stack.pop()
                    new_s.append(x)
                stack.pop()
                stack.append(''.join(new_s))
                i += 1
            elif c.isdigit():
                stack.append(c)
                i += 1
                while i < len(s) and s[i].isdigit():
                    x = stack.pop()
                    stack.append(s[i] + x)
                    i += 1
                x = stack.pop()
                y = stack.pop()
                stack.append(y * int(x))
            else:
                stack.append(c)
                i += 1

        return ''.join(reversed(stack))
            