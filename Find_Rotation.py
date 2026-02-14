class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for _ in range(4):
            temp = copy.deepcopy(mat)
            for i in range(n):
                temp[i] = [row[::-1][i] for row in mat]
            print(temp)
            if temp == target:
                return True
            mat = copy.deepcopy(temp)

        return False
