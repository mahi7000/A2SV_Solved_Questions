def countZeroes(n, x, k, s):
    i = 0
    while k > 0 and i < n:
        x += 1 if s[i] == "R" else -1
        k -= 1
        i += 1
        if x == 0:
            i = 0
            break
    else:
        return 0
 
    k1 = k
    while k > 0 and i < n:
        x += 1 if s[i] == "R" else -1
        k -= 1
        i += 1
        if x == 0:
            break
    else:
        return 1
    
    return (k1 // i) + 1
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x, k = map(int, input().split())
        s = input()
        print(countZeroes(n, x, k, s))
