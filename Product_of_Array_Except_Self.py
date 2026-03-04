class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suff = [], []

        acc = 1
        for num in nums:
            pref.append(acc)
            acc *= num

        acc = 1
        for num in nums[::-1]:
            suff.append(acc)
            acc *= num

        ans = []
        for a, b in zip(pref, suff[::-1]):
            ans.append(a * b)

        return ans
