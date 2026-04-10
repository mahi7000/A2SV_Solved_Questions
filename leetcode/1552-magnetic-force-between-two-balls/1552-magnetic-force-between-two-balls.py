class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def validate(x):
            prev = position[0]
            placed = 1

            for i in range(1, len(position)):
                if position[i] - prev >= x:
                    placed += 1
                    prev = position[i]

                if placed == m:
                    return True

            return False

        position.sort()
        distances = set([position[i] - position[i - 1] for i in range(1, len(position))])

        low = min(distances)
        maxx, minn = max(position), min(position)
        high = maxx - minn

        while low <= high:
            mid = (low + high) // 2

            if validate(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high