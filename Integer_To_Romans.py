class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

        s = []
        for roman, i in zip(romans, ints):
            while num >= i:
                num -= i
                s.append(roman) 

        return "".join(s)
