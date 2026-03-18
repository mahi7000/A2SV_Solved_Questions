import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    bob = arr[-1]

    count = 0

    for i in range(2, n):
        l, r = 0, i - 1

        while l < r:
            # if i != n - 1 and arr[l] + arr[r] + arr[i] > bob:
            #     count += 1


            if arr[l] + arr[r] + arr[i] <= bob:
                l += 1
            else:
                if arr[l] + arr[r] > arr[i]:
                    count += r - l 
                    r -= 1
                else:
                    l += 1

    print(count)