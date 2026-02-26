n, s = map(int, input().split())
arr = list(map(int, input().split()))

r = 0
summ = 0
w = 0

for l in range(n):
    while r < n and summ < s:
        summ += arr[r]
        r += 1

    if summ >= s:
        w += n - r + 1
    summ -= arr[l]

print(w)
