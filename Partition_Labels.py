class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alpha = [0] * 26

        for i, c in enumerate(s):
            alpha[ord(c) - ord('a')] = i

        sizes = []
        start = 0
        end = 0

        for i, c in enumerate(s):
            end = max(end, alpha[ord(c) - ord('a')])

            if i == end:
                sizes.append(end - start + 1)
                start = i + 1

        return sizes
