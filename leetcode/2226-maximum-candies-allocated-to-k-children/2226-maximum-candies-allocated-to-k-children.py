class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def validate(mid):
            if mid == 0:
                return True

            count = 0
            for candy in candies:
                count += candy // mid

            if count >= k:
                return True
            return False

        if sum(candies) < k:
            return 0

        low, high = 0, max(candies)
        while low <= high:
            mid = (low + high) // 2

            if validate(mid):
                low = mid + 1
            else: 
                high = mid - 1

        return high