if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        arr = []
        for _ in range(n):
            arr.append(tuple(map(int, input().split())))

        arr.sort(key=lambda x: x[0])

        for l, r, coin in arr:
            if l <= k <= r:
                k = max(k, coin)

        print(k)
