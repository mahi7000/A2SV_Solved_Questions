class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)

        result = set()
        for key in nums_counter:
            if nums_counter[key] > len(nums) // 3:
                result.add(key)

        return list(result)
