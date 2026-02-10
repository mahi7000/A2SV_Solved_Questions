class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start, col_start = 0, 0
        row_end, col_end = len(matrix), len(matrix[0])

        result = []
        while row_start < row_end and col_start < col_end:
            if row_start < row_end and col_start < col_end:
                result.extend(matrix[row_start][col_start: col_end])
                row_start += 1
            else:
                break

            if row_start < row_end and col_start < col_end:
                result.extend([row[col_end - 1] for row in matrix[row_start:row_end]])
                col_end -= 1
            else:
                break

            if row_start < row_end and col_start < col_end:
                result.extend(matrix[row_end - 1][col_start: col_end][::-1])
                row_end -= 1
            else:
                break

            if row_start < row_end and col_start < col_end:
                result.extend([row[col_start] for row in matrix[row_start:row_end]][::-1])
                col_start += 1
            else:
                break

        return result
