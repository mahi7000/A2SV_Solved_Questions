def findMinLength(n, s):
    prefix_a = [0] * (n + 1)
    prefix_b = [0] * (n + 1)
    prefix_c = [0] * (n + 1)
    
    for i in range(n):
        prefix_a[i + 1] = prefix_a[i] + (1 if s[i] == 'a' else 0)
        prefix_b[i + 1] = prefix_b[i] + (1 if s[i] == 'b' else 0)
        prefix_c[i + 1] = prefix_c[i] + (1 if s[i] == 'c' else 0)
    
    for length in range(2, 8):
        if length > n:
            break
        
        for i in range(n - length + 1):
            a_count = prefix_a[i + length] - prefix_a[i]
            b_count = prefix_b[i + length] - prefix_b[i]
            c_count = prefix_c[i + length] - prefix_c[i]
            
            if a_count > b_count and a_count > c_count:
                return length
    
    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        print(findMinLength(n, s))
