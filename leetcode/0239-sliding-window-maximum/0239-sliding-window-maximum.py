class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []

        for i, num in enumerate(nums):
            while queue and num > nums[queue[-1]]:
                queue.pop()
            if queue and i - k >= queue[0]:
                queue.popleft()
            queue.append(i)
            res.append(nums[queue[0]])

        return res[k - 1:]