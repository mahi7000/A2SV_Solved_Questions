class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num, prev = 0, 0

        for c in reversed(s):
            if prev > roman_to_int[c]:
                num -= roman_to_int[c]
            else:
                num += roman_to_int[c]
            prev = roman_to_int[c]

        return num
