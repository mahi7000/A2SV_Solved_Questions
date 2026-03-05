from collections import defaultdict
n, k, q = map(int, input().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

b = []
for _ in range(q):
    b.append(list(map(int, input().split())))


pref = [0] * 200001
for l, r in a:
    pref[l] += 1
    if r + 1 < 200001:
        pref[r + 1] -= 1

acc = 0
for i in range(200001):
    acc += pref[i]
    pref[i] = acc

x = [0] * 200001
for i in range(200001):
    if pref[i] >= k:
        x[i] += 1

acc = 0
for i in range(200001):
    acc += x[i]
    x[i] = acc



for l, r in b:
    print(x[r] - x[l - 1])
