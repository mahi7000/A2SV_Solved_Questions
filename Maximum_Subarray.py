class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minn = 0
        maxx = float("-inf")

        summ = 0
        for num in nums:
            summ += num
            maxx = max(maxx, summ - minn)
            minn = min(minn, summ)

        return maxx
