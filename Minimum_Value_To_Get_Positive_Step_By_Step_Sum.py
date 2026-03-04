class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minn = float("inf")

        summ = 0
        for num in nums:
            summ += num
            minn = min(minn, summ)

        x = 1 - minn

        return 1 if x <= 0 else x
