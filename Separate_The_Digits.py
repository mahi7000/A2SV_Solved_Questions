class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums = "".join(list(map(str, nums)))

        return list(map(int, list(nums)))
