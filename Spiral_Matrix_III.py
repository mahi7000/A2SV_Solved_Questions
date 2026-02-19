class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        res = []

        step = 1
        side = 0

        while len(res) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                        res.append([rStart, cStart])
                    rStart += direction[side][0]
                    cStart += direction[side][1]
                side = (side + 1) % 4
            step += 1
        
        return res
