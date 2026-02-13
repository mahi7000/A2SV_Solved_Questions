class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        smoothed_img = [[0 for j in row] for row in img]

        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(n):
            for j in range(m):
                count = 0
                for x, y in moves:
                    if i + x >= 0 and j + y >= 0 and i + x < n and j + y < m:
                        smoothed_img[i][j] += img[i + x][j + y]
                        count += 1
                smoothed_img[i][j] //= count

        return smoothed_img
