from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    t = list(input())

    t.sort()
    t_count = Counter(t)

    f = True
    for k, v in Counter(s).items():
        if k not in t_count or v > t_count[k]:
            f = False
            print("Impossible")
            break
        t_count[k] -= v

    if f:
        t = []
        for k, v in t_count.items():
            t.extend([k] * v)

        res = []
        p = 0
        count = 0
        for c in s:
            while p < len(t) and t[p] < c:
                res.append(t[p])
                p += 1
            res.append(c)
            count += 1

        res.extend(t[p:])


        print(''.join(res))
