class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        if target > nums[pivot] and target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        elif target > nums[-1]:
            left = 0
            right = pivot
        elif target == nums[pivot]:
            return pivot
        
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1