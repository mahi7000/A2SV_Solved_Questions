def findOperations(n, a, b):
    ops = []
    # count = 0
    # for i in range(n):
    #     for j in range(n - i - 1):
    #         if a[j] % 2 == 0:
    #             a[j], a[j + 1] = a[j + 1], a[j]
    #             ops.append([1, j + 1])
    #             count += 1
    #         if b[j] % 2 == 1:
    #             b[j], b[j + 1] = b[j + 1], b[j]
    #             ops.append([2, j + 1])
    #             count += 1

    # print(a)
    # print(b)

    # for i in range(n - 1, -1, -1):
    #     if a[i] % 2 == 1:
    #         break
    #     a[i], b[i] = b[i], a[i]
    #     ops.append([3, i + 1])

    # print(a)
    # print(b)

    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ops.append([1, j + 1])
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                ops.append([2, j + 1])

    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            ops.append([3, i + 1])

    # print(a)
    # print(b)

    return ops

    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))


        ops = findOperations(n, a, b)
        print(len(ops))
        for op in ops:
            print(*op)
