class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        n = len(digits)
        mapp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def com(i, arr):
            if i == n:
                ans.append("".join(arr))
                return

            for c in mapp[digits[i]]:
                arr.append(c)
                com(i + 1, arr)
                arr.pop()

        com(0, [])
        return ans