class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        count = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                return 

            grid[row][col] = '0'
            for x, y in directions:
                nrow = row + y
                ncol = col + x

                dfs(nrow, ncol)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)

        return count

   