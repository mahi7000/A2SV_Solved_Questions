seq = input()
stack = [-1]
maxx = 0
count = 0

for i, b in enumerate(seq):
    if b == "(":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            if maxx < i - stack[-1]:
                maxx = i - stack[-1]
                count = 1
            elif maxx == i - stack[-1]:
                count += 1

if maxx == 0:
    print(0, 1)
else:
    print(maxx, count)