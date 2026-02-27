from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
unique = 0
freq = defaultdict(int)

left = 0
for right in range(n):
    freq[arr[right]] += 1
    if freq[arr[right]] == 1:
        unique += 1
    
    while unique > k:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            # del freq[arr[left]]
            unique -= 1
        left += 1

    count += right - left + 1

print(count)
