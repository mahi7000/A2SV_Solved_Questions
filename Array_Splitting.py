if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ranges = []
    for i in range(n - 1):
        ranges.append(arr[i + 1] - arr[i])

    ranges.sort()

    cost = sum(ranges[:n - k])
    print(cost)
