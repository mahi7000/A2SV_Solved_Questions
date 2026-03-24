# from collections import 

# n = int(input())
# arr = {1: 0}
# for i in range(n - 1):
#     arr[i + 1] = int(input())
#     if arr[i + 1] in arr:
#         del arr[i + 1]

# if len(arr) == n - 1:
#     print("YES")
# else:
#     print("NO")

from collections import deque
n = int(input())
tree = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    tree[int(input())].append(i)

queue = deque([1])
while queue:
    node = queue.popleft()
    count = 0
    for child in tree[node]:
        if not tree[child]:
            count += 1
        else:
            queue.append(child)

    if count < 3:
        print("No")
        exit(0)

print("Yes")