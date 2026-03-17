class Solution:
    def countGoodNumbers(self, n: int) -> int:
        one, two = n//2, ceil(n/2)
        def myPow(x: float, n: int) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x
                
            if n == -1:
                return 1 / x

            half = myPow(x, n // 2) 
            if n % 2 == 0:
                return (half * half) % (10 ** 9 + 7)
            return (half * half * x) % (10 ** 9 + 7)
        
        return (myPow(4, one) * myPow(5, two)) % (10 ** 9 + 7)