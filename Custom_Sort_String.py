class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        new_string = []

        for char in order:
            new_string.append(char * count[ord(char) - ord('a')])
            count[ord(char) - ord('a')] = 0

        for i, c in enumerate(count):
            new_string.append(chr(i + ord('a')) * c)

        return ''.join(new_string)
