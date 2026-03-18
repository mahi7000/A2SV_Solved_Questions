class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1

        res = (k + self.findTheWinner(n - 1, k)) % n

        if res == 0:
            return n
        else:
            return res