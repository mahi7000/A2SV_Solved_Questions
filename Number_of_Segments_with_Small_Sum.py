n, s = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
summ = 0
w = 0

for r in range(n):
    summ += arr[r]

    while summ > s:
        summ -= arr[l]
        l += 1

    w += r - l + 1

print(w)
