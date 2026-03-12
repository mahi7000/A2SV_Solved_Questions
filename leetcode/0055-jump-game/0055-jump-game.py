class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        for num in nums:
            if i < 0:
                return False
            i = max(num, i)
            i -= 1
            

        return True 