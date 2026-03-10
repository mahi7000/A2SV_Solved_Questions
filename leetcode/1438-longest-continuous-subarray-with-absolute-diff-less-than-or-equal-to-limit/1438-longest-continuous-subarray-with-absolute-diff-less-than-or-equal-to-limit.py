class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()
        maxx = 0

        for i, num in enumerate(nums):
            while inc and abs(num - inc[0][0]) > limit:
                inc.popleft()
            while dec and abs(num - dec[0][0]) > limit:
                dec.popleft()
            mn, mx = i, i
            while inc and inc[-1][0] > num:
                mn = inc[-1][1]
                inc.pop()
            while dec and dec[-1][0] < num:
                mx = dec[-1][1]
                dec.pop()

            inc.append(tuple([num, mn]))
            dec.append(tuple([num, mx]))

            lens = min(i - inc[0][1] + 1, i - dec[0][1] + 1)
            maxx = max(maxx, lens)

        return maxx