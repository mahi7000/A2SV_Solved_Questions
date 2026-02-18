class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_dict = {}

        for i, num in enumerate(nums):
            nums_dict[i] = (str(num) * 20)[:20]
        
        nums_dict = dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))

        num = ""
        for i in nums_dict.keys():
            num += str(nums[i])

        return num if num[0] != "0" else "0"
