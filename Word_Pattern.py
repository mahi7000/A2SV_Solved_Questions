class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern):
            return False

        match = {}
        words = set()

        for i, char in enumerate(pattern):
            if char in match:
                if match[char] != s[i]:
                    return False
            else:
                if s[i] in words:
                    return False
                words.add(s[i])
                match[char] = s[i]

        return True
