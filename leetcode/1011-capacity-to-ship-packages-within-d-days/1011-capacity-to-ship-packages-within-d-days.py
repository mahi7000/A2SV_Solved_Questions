class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(capacity):
            count, summ = 1, 0
            for weight in weights:
                summ += weight
                if summ > capacity:
                    count += 1
                    summ = weight

            if count <= days:
                return True
            return False

        low, high = max(weights), sum(weights)

        while low <= high:
            mid = (low + high) // 2

            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low