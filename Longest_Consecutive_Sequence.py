class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        
        if len(nums) == 1:
            return 1

        left = 0
        longest = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left] + right - left:
                left = right
            longest = max(longest, right - left + 1)

        return longest
