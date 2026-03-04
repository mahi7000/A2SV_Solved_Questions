class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = defaultdict(int)
        mapp[0] = 1

        count = 0
        summ = 0
        for num in nums:
            summ += num
            count += mapp[summ - k]
            mapp[summ] += 1

        return count
