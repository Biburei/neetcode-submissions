class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            current = min(heights[left], heights[right]) * (right - left)
            area = max(current, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return area