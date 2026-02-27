class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq, max_size = 0, 0

        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            while r - l + 1 > max_freq + k:
                freq[s[l]] -= 1
                l += 1
            
            max_size = max(max_size, r - l + 1)

        return max_size
