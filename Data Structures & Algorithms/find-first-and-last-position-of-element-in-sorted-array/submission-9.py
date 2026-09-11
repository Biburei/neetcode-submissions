class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] != target:
                left += 1
            elif nums[right] != target:
                right -= 1
            else:
                return [left, right]
        return [-1, -1]
            