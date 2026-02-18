if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    k = 1
    count = 0
    for num in arr:
        if num < k:
            continue
        k += 1
        count += 1

    print(count)
