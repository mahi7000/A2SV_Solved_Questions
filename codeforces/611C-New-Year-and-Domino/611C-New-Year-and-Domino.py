h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input())

hor = [[0] * (w + 1) for _ in range(h + 1)]
ver = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        hor[i][j] = hor[i - 1][j] + hor[i][j - 1] - hor[i - 1][j - 1]
        ver[i][j] = ver[i - 1][j] + ver[i][j - 1] - ver[i - 1][j - 1]

        if j < w and grid[i - 1][j - 1] == '.' and grid[i - 1][j] == '.':
            hor[i][j] += 1

        if i < h and grid[i - 1][j - 1] == '.' and grid[i][j - 1] == '.':
            ver[i][j] += 1

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    x = hor[r2][c2 - 1] - hor[r1 - 1][c2 - 1] - hor[r2][c1 - 1] + hor[r1 - 1][c1 - 1]
    y = ver[r2 - 1][c2] - ver[r1 - 1][c2] - ver[r2 - 1][c1 - 1] + ver[r1 - 1][c1 - 1]

    print(x + y)