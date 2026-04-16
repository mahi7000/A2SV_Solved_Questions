class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()

        prev = nums[0]
        for num in nums[1:]:
            if num == prev:
                res.append(num)
                break
            prev = num

        nums = sorted(set(nums))
        for i, num in enumerate(nums):
            if i + 1 != num:
                res.append(i + 1)
                break

        return res if len(res) == 2 else [res[0], len(nums) + 1]