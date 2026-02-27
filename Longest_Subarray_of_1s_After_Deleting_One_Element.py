class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        max_size = 0

        l = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1

            while r - l > freq[1]:
                freq[nums[l]] -= 1
                l += 1

            max_size = max(max_size, r - l)

        return max_size
