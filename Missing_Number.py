class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i, num in enumerate(nums):
            print(i)
            print(num)
            if i != num:
                return i
        return i + 1
