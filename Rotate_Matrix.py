class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        temp_matrix = [[num for num in row] for row in matrix]

        for i in range(n):
            for j in range(n):
                new_row = j
                new_col = n - i - 1

                matrix[new_row][new_col] = temp_matrix[i][j]
