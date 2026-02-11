class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        nums_count = Counter(nums)

        for key, val in nums_count.items():
            if val > len(nums) // 2:
                dom_num = key
                dom_freq = val

        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == dom_num:
                count += 1
                if count > (i + 1) // 2 and dom_freq - count > (len(nums) - i - 1) // 2:
                    return i

        return -1
