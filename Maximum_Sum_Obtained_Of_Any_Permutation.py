class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()

        request = [0] * (len(nums))

        for l, r in requests:
            request[l] += 1
            if r + 1 < len(nums):
                request[r + 1] -= 1

        # print(request)

        acc = 0
        for i, r in enumerate(request):
            acc += r
            request[i] = acc
        request.sort()

        # print(request)

        summ = 0
        for i in range(len(nums)):
            summ += request[i] * nums[i]

        return summ % ((10 ** 9) + 7)
