t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))



    sub = [p[0]]
    pos = (p[1] - p[0]) >= 0
    placeholder = 0

    for s in range(2, n):
        if pos and (p[s] - p[s  - 1]) < 0:
            pos = False
            placeholder = s - 1
            sub.append(p[placeholder])
        elif not pos and (p[s] - p[s  - 1]) > 0:
            pos = True
            placeholder = s - 1
            sub.append(p[placeholder])

        # print(placeholder)
        # print(s)
        # print(pos)

    sub.append(p[-1])

    print(len(sub))
    print(*sub)
