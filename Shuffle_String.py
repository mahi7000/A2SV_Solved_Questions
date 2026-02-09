class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        rearranged = list(s)

        for i, ss in zip(indices, s):
            rearranged[i] = ss

        return "".join(rearranged)
