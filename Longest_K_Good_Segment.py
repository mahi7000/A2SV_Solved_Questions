from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

unique = 0
freq = defaultdict(int)
left = 0
max_range = [0, -1]

for right in range(n):
    freq[a[right]] += 1
    if freq[a[right]] == 1:
        unique += 1

    while unique > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            unique -= 1
        left += 1

    if unique <= k and right - left > max_range[1] - max_range[0]:
            max_range = [left + 1, right + 1]

print(*max_range)
