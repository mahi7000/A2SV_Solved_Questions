class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods = [0]
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            mods.append(summ % k)

        # print(mods)

        mapp = {}
        for i, mod in enumerate(mods):
            if mod in mapp:
                if i - mapp[mod] >= 2:
                    return True
            if mod not in mapp:
                mapp[mod] = i

        # print(mapp)

        return False
