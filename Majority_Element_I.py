class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums_count = Counter(nums)

        ans = []
        for num, count in nums_count.items():
            if count > n / 3:
                ans.append(num)

        return ans
