class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)

        for key, value in nums_counter.items():
            if value == 1:
                return key
