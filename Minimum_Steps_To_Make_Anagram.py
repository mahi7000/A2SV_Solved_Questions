class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)

        match_chars = 0
        for key, val in s_count.items():
            if key in t_count:
                match_chars += min(val, t_count[key])

        return len(s) - match_chars
