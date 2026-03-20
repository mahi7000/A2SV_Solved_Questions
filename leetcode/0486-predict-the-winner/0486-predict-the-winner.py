class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(turn, l, r):
            if l > r:
                return 0

            if turn:
                turn = not turn
                return max(nums[l] + predict(turn, l + 1, r), nums[r] + predict(turn, l, r - 1))
            turn = not turn
            return min(predict(turn, l + 1, r) - nums[l], predict(turn, l, r - 1) - nums[r])


        return True if predict(True, 0, len(nums) - 1) >= 0 else False