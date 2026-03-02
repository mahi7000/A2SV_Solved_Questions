class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left = 0
        freq = defaultdict(int)

        unique = 0
        count = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            c = freq[nums[right]]
            if freq[nums[right]] == 1:
                unique += 1

            while unique > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    unique -= 1
                left += 1
            count += right - left + 1

        left = 0
        freq = defaultdict(int)

        unique = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            c = freq[nums[right]]
            if freq[nums[right]] == 1:
                unique += 1

            while unique > k - 1:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    unique -= 1
                left += 1
            count -= right - left + 1

        return count
