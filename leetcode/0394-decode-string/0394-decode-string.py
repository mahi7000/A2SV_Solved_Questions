class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        for i in range(len(s)):
            if stack and stack[-1].isdigit() and s[i].isdigit():
                stack.append(stack.pop() + s[i])
            elif stack and stack[-1].islower() and s[i].islower():
                stack.append(stack.pop() + s[i])
            elif s[i] == ']':
                x = stack.pop()
                y = stack.pop()
                z = stack.pop()
                if stack and stack[-1].isalpha():
                    w = stack.pop()
                    stack.append(w + x * int(z))
                else:
                    stack.append(x * int(z))
            else:
                stack.append(s[i])
                
        return ''.join(stack)
