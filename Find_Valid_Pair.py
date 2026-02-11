class Solution:
    def findValidPair(self, s: str) -> str:
        s_count = Counter(s)
        left, right = 0, 1

        while right < len(s):
            if s_count[s[left]] == int(s[left]) and s_count[s[right]] == int(s[right]) and s[right] != s[left]:
                return s[left] + s[right]

            if s_count[s[right]] != int(s[right]):
                left = right + 1
            else:
                left = right
            right = left + 1

        return ""
