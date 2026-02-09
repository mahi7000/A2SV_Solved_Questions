class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_place = {}
        for i, num in enumerate(nums):
            if target - num in num_place:
                return [i, num_place[target - num]]
            num_place[num] = i

        return []

