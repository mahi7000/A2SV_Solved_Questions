t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))

    acc = 0
    for i in range(n):
        acc += r[i]
        r[i] = acc
    r.append(0)

    m = int(input())
    b = list(map(int, input().split()))

    acc = 0
    for i in range(m):
        acc += b[i]
        b[i] = acc
    b.append(0)

    print(max(r) + max(b))
