class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        low, high = 0, (n * m) - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // m
            col = mid % m

            mat = matrix[row][col]
            if mat < target:
                low = mid + 1
            elif mat > target:
                high = mid - 1
            else:
                return True

        return False