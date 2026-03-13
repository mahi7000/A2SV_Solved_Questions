class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1 and maxDoubles:
            if target % 2 == 0 and maxDoubles:
                target /= 2
                maxDoubles -= 1
            else:
                target -= 1
            count += 1

        count += target - 1

        return int(count)