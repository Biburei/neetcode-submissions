class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        total = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                total += 1
                left += 1
                nums[left] = nums[right]
        return total + 1