class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def com(i, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return

            for j in range(i, n + 1):
                arr.append(j)
                com(j + 1, arr)
                arr.pop()

        com(1, [])
        return ans