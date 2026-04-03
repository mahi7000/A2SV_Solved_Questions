class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permutation(arr, sett):
            if len(arr) == len(nums):
                res.append(arr[:])
                return

            for num in nums:
                if num in sett:
                    arr.append(num)
                    sett.remove(num)
                    permutation(arr, sett)
                    sett.add(num)
                    arr.pop()

        permutation([], set(nums))
        return res