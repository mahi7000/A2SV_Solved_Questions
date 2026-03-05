class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mapp = defaultdict(int)
        mapp[0] = 1

        count = 0
        summ = 0
        for num in nums:
            summ += num
            count += mapp[summ - goal]
            mapp[summ] += 1

        return count
