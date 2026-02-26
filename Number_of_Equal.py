from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_count = Counter(a)
a_count = dict(sorted(a_count.items(), key=lambda x: x[0]))

p = 0
ans = 0
for k, v in a_count.items():
    if p == len(b):
        break
        
    count = 0
    while p < len(b) and k >= b[p]:
        if k == b[p]:
            count += 1
        p += 1

    ans += count * v

print(ans)
