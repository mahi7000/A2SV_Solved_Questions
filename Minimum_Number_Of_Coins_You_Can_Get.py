class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)

        ans = 0
        for i in range(1, (n // 3) + 1):
            ans += piles[n - (2 * i)]

        return ans
