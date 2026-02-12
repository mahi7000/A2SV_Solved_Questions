class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = []
        rows = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.append(j)
                    rows.append(i)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in cols:
                    matrix[i][j] = 0
                if i in rows:
                    matrix[i][j] = 0
