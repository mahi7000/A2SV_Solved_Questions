class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        rabbits = Counter(answers)

        for rabbit, count in rabbits.items():
            rabbit += 1
            res += ceil(count / rabbit) * rabbit

        return res