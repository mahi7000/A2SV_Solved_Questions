class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []

        if len(changed) % 2 == 1:
            return []

        changed.sort()

        count = Counter(changed)

        for num in changed:
            if count[num] == 0:
                continue
            else:
                if count.get(num * 2, 0) >= 1:
                    original.append(num)
                    count[num * 2] -= 1
                    count[num] -= 1
                else:
                    return []

        return original
