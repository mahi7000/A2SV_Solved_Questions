class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        acc = 0
        for i, num in enumerate(nums):
            acc += nums[i]
            nums[i] = acc % k


        mapp = defaultdict(int)
        mapp[0] = 1

        count = 0
        for num in nums:
            count += mapp[num]
            mapp[num] += 1

        return count
