class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        count = defaultdict(int)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                x = stack.pop()
                count[x] = i - x
            stack.append(i)

        return [count[i] for i in range(len(temperatures))]