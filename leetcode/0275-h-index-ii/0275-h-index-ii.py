class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def validate(mid):
            return citations[mid] <= len(citations) - mid

        low, high = 0, len(citations) - 1
        while low <= high:
            mid = (low + high) // 2

            if citations[mid] == len(citations) - mid:
                return citations[mid]

            if validate(mid):
                low = mid + 1
            else:
                high = mid - 1

        return len(citations) - low