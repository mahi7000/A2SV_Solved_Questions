class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))

        while left <= right:
            calc = (left ** 2) + (right ** 2)
            if calc == c:
                return True

            if calc < c:
                left+= 1
            else:
                right -= 1

        return False
