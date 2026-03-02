t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input())
    b = list(input())

    zero = a.count('0')
    one = n - zero

    flipped = False
    f = True

    a.reverse()
    b.reverse()
    # print(a)
    # print(b)

    for i, num in enumerate(a):
        # print(num, b[i])
        # print(zero, one)
        # print(flipped)
        if (zero != one) and ((not flipped and num != b[i]) or (flipped and num == b[i])):
            f = False
            break

        if (flipped and (num == b[i])) or (not flipped and (num != b[i])):
            flipped = not flipped
        
        if b[i] == '0':
            zero -= 1
        else:
            one -= 1

    if f:
        print("YES")
    else:
        print("NO")
