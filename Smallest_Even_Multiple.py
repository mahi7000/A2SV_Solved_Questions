class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        smallest = n
        while True:
            if smallest % n == 0 and smallest % 2 == 0:
                return smallest
            smallest += 1
