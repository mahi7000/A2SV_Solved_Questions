class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        def nqueens(board, sett):
            if len(board) == n:
                self.ans.append(board[:])
                return


            for i in range(n):
                ans = ['.'] * n
                ans[i] = 'Q'
                f = False

                for row, col in sett:
                    if abs(i - row) == abs(len(board) - col) or row == i:
                        f = True
                        break

                if f:
                    continue

                sett.add((i, len(board)))
                board.append(''.join(ans))
                nqueens(board,sett)
                board.pop()
                sett.remove((i, len(board)))

        nqueens([], set())
        return self.ans