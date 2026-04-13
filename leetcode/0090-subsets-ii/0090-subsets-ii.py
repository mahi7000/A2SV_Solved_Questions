class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def subset(arr, i):
            res.append(arr[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                arr.append(nums[j])
                subset(arr, j + 1)
                arr.pop()


        nums.sort()
        res = []
        subset([], 0)
            
        return res