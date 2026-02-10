class Solution:
    def isHappy(self, n: int) -> bool:
        while n >= 10:
            res = 0
            n = list(map(int, str(n)))
            for i in n:
                res += i ** 2
            n = res
        return n == 1 or n == 7
