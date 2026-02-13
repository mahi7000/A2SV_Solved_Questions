class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        diagonal = []

        move = 0
        row, col = 0, 0
        for _ in range(m + n - 1):
            i, j = row, col
            while move and i < n and j >= 0:
                diagonal.append(mat[i][j])
                row, col = i, j
                i += 1
                j -= 1
            
            while not move and i >= 0 and j < m:
                diagonal.append(mat[i][j])
                row, col = i, j
                i -= 1
                j += 1

            if move:
                if row < n - 1:
                    row += 1
                else:
                    col += 1
            else:
                if col < m - 1:
                    col += 1
                else:
                    row += 1

            move += -1 if move else 1

        return diagonal
