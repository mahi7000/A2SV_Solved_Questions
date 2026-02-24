t = int(input())
for _ in range(t):
    s = input()
    i = 0
    arr = set()
    while i < len(s):
        if i + 1 < len(s):
            if s[i] == s[i + 1]:
                i += 1
            else:
                arr.add(s[i])
        else:
            arr.add(s[i])

        i += 1

    print(''.join(sorted(arr)))
