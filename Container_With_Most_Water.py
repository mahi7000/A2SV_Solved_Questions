class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)
            # left_area = min(height[left + 1], height[right]) * (right - (left + 1))
            # right_area = min(height[left], height[right - 1]) * (right - left - 1)

            # if max(left_area, right_area) <= area:
            #     return area

            # if left_area > right_area:
            #     left += 1
            # else:
            #     right += 1
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
