class Solution:
    def lastRemaining(self, n: int) -> int:
        def check(n, dire):
            if n == 1:
                return 1

            if dire:
                return 2 * check(n // 2, not dire)

            if n % 2:
                return 2 * check(n // 2, not dire)
            return 2 * check(n // 2, not dire) - 1

        return check(n, True)