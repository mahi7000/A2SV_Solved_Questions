class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0

        def queens(sett):
            if len(sett) == n:
                self.count += 1
                return

            for i in range(n):
                f = False
                for row, col in sett:
                    if i == row or abs(i - row) == abs(len(sett) - col):
                        f = True
                        break
                if f:
                    continue


                sett.add((i, len(sett)))
                queens(sett)
                sett.remove((i, len(sett) - 1))

        queens(set())
        return self.count