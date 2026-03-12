class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = deque(nums)

        count = 0
        while nums:
            n = nums.popleft()
            if n == 0:
                if len(nums) < 2:
                    return -1
                for i in range(2):
                    nums[i] = 0 if nums[i] else 1
                count += 1

        return count