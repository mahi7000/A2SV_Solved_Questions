class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        prev = []

        for i, height in enumerate(heights):
            while stack and stack[-1] != -1 and heights[stack[-1]] >= height:
                stack.pop()
            prev.append(abs(stack[-1] - len(heights) + 1))
            stack.append(i)

        stack = [-1]
        heights.reverse()
        max_area = 0
        for i, height in enumerate(heights):
            while stack and stack[-1] != -1 and heights[stack[-1]] >= height:
                stack.pop()
            area = height * (prev[len(heights) - i - 1] - stack[-1] - 1)
            # print(area)
            stack.append(i)
            max_area = max(max_area, area)

        return max_area