t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))
 
    left = sorted(socks[:l])
    right = sorted(socks[l: l + r])
 
    ops = abs((n // 2) - l)
 
    l_i, r_i = 0, 0
 
    # print(left, right)
 
    same = 0
    while l_i < l and r_i < r:
        if left[l_i] < right[r_i]:
            l_i += 1
        elif left[l_i] > right[r_i]:
            r_i += 1
        else:
            left[l_i] = 0
            right[r_i] = 0
            l_i += 1
            r_i += 1
            same += 1

    left_arr = []
    for num in left:
        if num != 0:
            left_arr.append(num)

    right_arr = []
    for num in right:
        if num != 0:
            right_arr.append(num)
 
    # print(left, right)
 
    dup = 0
    if l > r:
        prev = 0
        for num in left_arr:
            if num == prev:
                prev = 0
                dup += 1
            else:
                prev = num
            if ops == dup:
                break
    elif l < r:
        prev = 0
        for num in right_arr:
            if num == prev:
                prev = 0
                dup += 1
            else:
                prev = num
            if ops == dup:
                break
 
    # print(dup)
 
    ops += (n // 2) - same - dup
    print(ops)
