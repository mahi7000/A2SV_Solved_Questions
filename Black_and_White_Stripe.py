from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    freq = defaultdict(int)
    for c in s[:k]:
        freq[c] += 1
    
    min_size = freq['W']
    for right in range(k, n):
        freq[s[right - k]] -= 1
        freq[s[right]] += 1

        min_size = min(min_size, freq['W'])

    print(min_size)
        
