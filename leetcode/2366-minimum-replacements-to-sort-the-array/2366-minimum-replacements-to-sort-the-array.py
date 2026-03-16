class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0

        prev = nums[-1]
        for num in nums[::-1]:
            if num <= prev:
                prev = num
                continue
            k = (num + prev - 1) // prev
            count += k - 1
            prev = num // k

        return count