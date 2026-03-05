class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix) + 1
        m = len(matrix[0]) + 1
        self.pref = [[0] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                self.pref[i][j] = matrix[i - 1][j - 1] + self.pref[i - 1][j] + self.pref[i][j - 1] - self.pref[i - 1][j - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = self.pref[row2 + 1][col2 + 1] - self.pref[row1][col2 + 1] - self.pref[row2 + 1][col1] + self.pref[row1][col1]

        return summ


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
