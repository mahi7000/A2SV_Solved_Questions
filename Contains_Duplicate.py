class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = set()

        for num in nums:
            if num in nums_count:
                return True
            nums_count.add(num)

        return False
