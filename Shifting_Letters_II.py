class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sh = [0] * (len(s) + 1)
        s = list(s)

        for l, r, d in shifts:
            sh[l] += 1 if d == 1 else -1
            sh[r + 1] += -1 if d == 1 else 1

        acc = 0
        for i, num in enumerate(sh):
            sh[i] += acc
            acc += num

        for i, c in enumerate(s):
            move = (ord(c) - ord('a') + sh[i]) % 26
            s[i] = chr(move + ord('a'))

        return ''.join(s)
